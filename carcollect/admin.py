from django.contrib import admin
from django.http import HttpResponse
from .models import Car, Brand, Category, Feature
from reportlab.pdfgen import canvas 
from reportlab.lib.pagesizes import A4
from io import BytesIO
import io
import base64
import matplotlib.pyplot as plt
from django.shortcuts import render
from django.urls import path
from django.db.models import Count


# Fonction pour générer le graphique
def stats_view(request):
    # Récupération des données : Nombre de voitures par marque
    data = Brand.objects.annotate(car_count=Count('cars'))
    labels = [b.name for b in data]
    counts = [getattr(b, 'car_count', 0) for b in data]

    # Création du graphique Matplotlib
    plt.figure(figsize=(8, 5))
    plt.bar(labels, counts, color='gold')
    plt.title('Nombre de voitures de luxe par marque')
    plt.xlabel('Marques')
    plt.ylabel('Quantité')

    # Conversion du graphique en image pour l'afficher en HTML
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    buffer.close()
    plt.close()

    return render(request, 'admin/stats.html', {'chart': image_base64})
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'category', 'power_hp', 'year', 'price')
    list_filter = ('brand', 'category', 'year')
    search_fields = ('model', 'brand__name')
    actions = ['export_as_pdf'] # On prépare l'action PDF ici
    
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('stats/', self.admin_site.admin_view(stats_view), name='carcollect_car_stats'),
        ]
        return custom_urls + urls
    
    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_stats_button'] = "True"
        return super().changelist_view(request, extra_context=extra_context)

    @admin.action(description="Exporter la fiche en PDF")
    def export_as_pdf(self, request, queryset):
        # Création d'un buffer en mémoire pour le PDF
        buffer = BytesIO()

        # Création du canvas ReportLab en écrivant dans le buffer
        p = canvas.Canvas(buffer, pagesize=A4)
        width, height = A4
        y = height - 50

        p.setFont("Helvetica-Bold", 18)
        p.drawString(100, y, "FICHE TECHNIQUE - COLLECTION DE LUXE")
        y -= 40

        for car in queryset:
            if y < 150: # Nouveau saut de page si on arrive en bas
                p.showPage()
                y = height - 50
            
            p.setFont("Helvetica-Bold", 14)
            p.drawString(100, y, f"{car.brand.name} {car.model}")
            p.setFont("Helvetica", 12)
            y -= 20
            p.drawString(120, y, f"• Catégorie : {car.category.name}")
            p.drawString(120, y-15, f"• Puissance : {car.power_hp} ch")
            p.drawString(120, y-30, f"• Année : {car.year}")
            p.drawString(120, y-45, f"• Prix : {car.price} €")
            y -= 80 # Espace entre deux voitures

        p.showPage()
        p.save()
        buffer.seek(0)

        # Création de la réponse HTTP avec le contenu du buffer
        response = HttpResponse(buffer.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="collection_luxe.pdf"'
        return response

        export_as_pdf.short_description = "Exporter les fiches en PDF"
        

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Feature)
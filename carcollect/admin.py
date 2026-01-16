from django.contrib import admin
from django.http import HttpResponse
from .models import Car, Brand, Category, Feature
from reportlab.pdfgen import canvas 
from reportlab.lib.pagesizes import A4
from io import BytesIO

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'category', 'power_hp', 'year', 'price')
    list_filter = ('brand', 'category', 'year')
    search_fields = ('model', 'brand__name')
    actions = ['export_as_pdf'] # On prépare l'action PDF ici

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
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from carcollect.views import CarViewSet
from django.views.generic import TemplateView

router = DefaultRouter()
router.register(r'cars', CarViewSet, basename='car')

urlpatterns = [
    path('admin/', admin.site.urls), # Garde ton admin existant
    path('api/', include('carcollect.urls')), 
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]
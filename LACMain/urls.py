from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from products import views
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('products/', views.all, name='products'),
    path('products/<slug:slug>', views.single, name='single_product'),


] 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    

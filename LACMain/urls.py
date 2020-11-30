from django.contrib import admin
from products import views
from django.urls import path



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('products/', views.all, name='products'),


]

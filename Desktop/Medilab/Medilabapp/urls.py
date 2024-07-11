#its a url page
from django.contrib import admin
from django.urls import path
from Medilabapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('start/', views.start, name='start'),
    path('service/', views.service, name='service'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('Appointment/', views.Appoint, name='Appointment'),
    path('Show/', views.Show, name='Show'),
    path('Delete/<int:id>', views.Delete, ),

]

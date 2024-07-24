#its a url page
from django.contrib import admin
from django.urls import path
from Medilabapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('start/', views.start, name='start'),
    path('service/', views.service, name='service'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('Appointment/', views.Appoint, name='Appointment'),
    path('Show/', views.Show, name='Show'),
    path('delete/<int:id>',views.delete,),
    path('edit/<int:id>',views.edit,),
    path('update/<int:id>',views.update,),
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
   path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),]



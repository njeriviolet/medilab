from django.contrib import admin
from Medilabapp.models import Product,Student,Patient,Appointment,Member

# Register your models here.
admin.site.register(Product)
admin.site.register(Student)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Member)
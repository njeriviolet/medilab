from django import forms
from Medilabapp.models import Appointment , Member

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'email', 'phone', 'date', 'department','doctor','message']
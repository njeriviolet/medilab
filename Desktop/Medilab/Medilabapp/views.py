from django.shortcuts import render, redirect
from Medilabapp.models import Appointment


#here i write my python functions to join front end and back end
# Create your views here.

def index(request):
    return render(request, 'index.html')


def start(request):
    return render(request, 'starter-page.html')


def service(request):
    return render(request, 'services.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contacts.html')


def Appoint(request):
    if request.method == 'POST':
        appointments = Appointment(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            date=request.POST['date'],
            department=request.POST['department'],
            doctor=request.POST['doctor'],
            message=request.POST['message'],

        )
        appointments.save()
        return redirect('/Appointment')
    else:
        return render(request, 'Appointment.html')

#to display data in form of a dctionary i need a key

def Show(request) :
    data =Appointment.objects.all()
    return render(request,'Show.html',{'appointment':data})


def Delete(request,id):
    myappointment = Appointment.objects.get(id=id)
    myappointment.delete()
    return redirect('/Show')
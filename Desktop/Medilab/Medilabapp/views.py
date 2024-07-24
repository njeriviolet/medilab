from django.contrib.sites import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect

from Medilabapp.credentials import MpesaAccessToken, LipanaMpesaPpassword
from Medilabapp.models import Appointment, Member
from Medilabapp.forms import AppointmentForm


# here i write my python functions to join front end and back end
# Create your views here.

def index(request):
    if request.method == 'POST':
        if Member.objects.filter(
                username=request.POST['name'],
                password=request.POST['password']).exists():
            member = Member.objects.get(name=request.POST['name'],password=request.POST['password'])
            return render(request, 'index.html',{'member':member})
        else:
            return render(request, 'login.html')

    else:
        return render(request, 'login.html')









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

#to display data in form of a dictionary i need a key

def Show(request) :
    data =Appointment.objects.all()
    return render(request , 'Show.html',{'appointment': data})


def delete(request,id):
    appointment = Appointment.objects.get(id=id)
    appointment.delete()
    return redirect('/Show')
def edit(request,id):
    appointment = Appointment.objects.get(id=id)
    return render(request,'edit.html',{'x':appointment})
def update(request,id):
    myappointment = Appointment.objects.get(id=id)
    form = AppointmentForm(request.POST,instance=myappointment)
    if form.is_valid():
        form.save()
        return redirect('/Show')
    else:
        return render(request,'edit.html')

def register(request):
    if request.method == 'POST':
        members = Member(
            name=request.POST['name'],
            username=request.POST['username'],
            password=request.POST['password'],
        )
        members.save()
        return redirect('/login')
    else :
        return render(request, 'register.html')

def login (request):
    return render(request, 'login.html')

def token(request, validated_mpesa_access_token=None):
    return render(request, 'token.html', {"token":validated_mpesa_access_token})

def pay(request):
   return render(request, 'pay.html')



def stk(request):
    if request.method =="POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "Apen Softwares",
            "TransactionDesc": "Web Development Charges"
        }
        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse("Success")



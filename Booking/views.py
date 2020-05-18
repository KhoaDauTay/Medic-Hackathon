from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request,"FormBooking.html")



def apponintment(request):
    if request.method == 'POST':
        Name = request.POST['Name']
        Age = request.POST['Age']
        phone = request.POST['phone']
        idCard = request.POST['idCardNumber']
        Address = request.POST['Address']
        City = request.POST['City']
        Province = request.POST['Province']
        Hostpital = request.POST['Hostpital']
        Date = request.POST['date']
        Time = request.POST['time']
        return render(request,'FormApointment.html', {'your_Name' : Name})
    else:
        return render(request,'base.html')
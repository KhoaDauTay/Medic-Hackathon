from django.shortcuts import render
from qrcode import *
# Create your views here.
data = None


def home(request):
    global data
    if request.method == 'POST':
        data = request.POST['data']
        img = make(data)
        img.save("static/image/QR_CODE4.png")

    else:
        pass
    return render(request, "finalform.html", {'data': data})
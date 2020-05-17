from django.urls import path
from.views import home

app_name ='QR_CODE'

urlpatterns = [
    path('', home, name='home'),
    path('send', home, name='home'),


]
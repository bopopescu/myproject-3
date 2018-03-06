from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse, request, HttpResponseRedirect
from cloudproject.models import *


class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

def SignupView(request):
    if request.method == "POST":
        emailid = request.POST['email']
        username = request.POST['uname']
        password = request.POST['pwd']
        entry(emailid, username, password)

        return render(request, 'signup.html')
    else:
        return render(request, 'signup.html')

def SigninView(request):
    if request.method == "POST":
        emailid = request.POST['email']
        password = request.POST['pwd']
        check = validate(emailid, password)
        if (check == 1):
            return HttpResponseRedirect("")
        if (check == 2):
            return HttpResponseRedirect("/signin/room/")
        else:
            return render(request, 'signin.html', {'error': 'Username or password incorrect'})
    else:
        return render(request, 'signin.html')

def RoomView(request):
    return render(request, 'room.html',context=None)

def AddRoomView(request):
    if request.method == "POST":
        capacity = request.POST['capacity']
        rtype = request.POST['type']
        price = request.POST['price']
        availability = request.POST['availability']
        addRoom(rtype,price,availability,capacity)

        return render(request, 'addroom.html')
    else:
        return render(request, 'addroom.html')


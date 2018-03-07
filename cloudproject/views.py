from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.views.generic import TemplateView
from django.http import HttpResponse, request, HttpResponseRedirect
from cloudproject.models import *


def HomePageView(request):
    return render(request, 'index.html', context=None)


def SignupView(request):
    if 'name' not in request.session:
        if 'name1' not in request.session:
            if request.method == "POST":
                emailid = request.POST['email']
                username = request.POST['uname']
                password = request.POST['pwd']
                entry(emailid, username, password)

                if request.POST['uname'] == 'admin':
                    return render(request, 'signup.html', {'error': 'Cant take this username'})

                return HttpResponseRedirect("/signin")
            else:
                return render(request, 'signup.html')
        else:
            return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/")


def SigninView(request):
    if 'name' not in request.session:
        if 'name1' not in request.session:
            if request.method == "POST":
                username = request.POST['uname']
                password = request.POST['pwd']
                check = validate(username, password)

                if check == 1:
                    request.session['name'] = username
                    return HttpResponseRedirect("/signin/user/")

                if check == 2:
                    request.session['name1'] = username
                    return HttpResponseRedirect("/signin/room/")

                else:
                    return render(request, 'signin.html', {'error': 'Username or password incorrect'})
            else:
                return render(request, 'signin.html')
        else:
            return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/")


def RoomView(request):
    if 'name1' in request.session:
        return render(request, 'room.html', context=None)
    else:
        return HttpResponseRedirect("/")


def UserView(request):
    if 'name' in request.session:
        return render(request, 'user.html', context=None)
    else:
        return HttpResponseRedirect("/")


def AddRoomView(request):
    if 'name1' in request.session:
        if request.method == "POST":
            capacity = request.POST['capacity']
            rtype = request.POST['type']
            price = request.POST['price']
            try:
                availability = request.POST['availability']
            except MultiValueDictKeyError:
                availability = "off"
            addRoom(rtype, price, availability, capacity)

            return render(request, 'addroom.html', {'error': 'Room added'})
        else:
            return render(request, 'addroom.html')
    else:
        return HttpResponseRedirect("/")


def RemoveRoomView(request):
    if 'name1' in request.session:
        if request.method == "POST":
            roomid = request.POST['roomid']
            id = int(roomid)

            check = delroom(id)
            if (check == 1):
                return render(request, 'removeroom.html', {'error': 'Room deleted'})
            else:
                return render(request, 'removeroom.html', {'error': 'No room found'})
        else:
            return render(request, 'removeroom.html')
    else:
        return HttpResponseRedirect("/")


def UpdatePriceView(request):
    if 'name1' in request.session:
        if request.method == "POST":
            roomid = request.POST['roomid']
            id = int(roomid)
            price = request.POST['price']

            check = updateprice(id, price)
            if (check == 1):
                return render(request, 'updateprice.html', {'error': 'Room price updated'})
            else:
                return render(request, 'updateprice.html', {'error': 'No room found'})
        else:
            return render(request, 'updateprice.html')
    else:
        return HttpResponseRedirect("/")


def BookRoomView(request):
    if 'name' in request.session:
        if request.method == "POST":
            rtype = request.POST['type']
            checkin = request.POST['date']
            days = request.POST['days']
            user = request.session.get('name')

            roomId = findRoom(rtype)

            if roomId == 0:
                return render(request, 'bookroom.html', {'error': 'Room not available'})
            else:
                bookRoom(user, roomId, rtype, checkin, days)
                availOff(roomId)

            return render(request, 'bookroom.html', {'error': 'Room booked'})
        else:
            return render(request, 'bookroom.html')
    else:
        return HttpResponseRedirect("/")


def LogoutView(request):
    if 'name1' in request.session:
        del request.session['name1']
    if 'name' in request.session:
        del request.session['name']

    return render(request, 'index.html', context=None)

from django.conf.urls import url
from cloudproject import views

app_name='cloudproject'

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^signup/', views.SignupView , name="SignupView"),
    url(r'^signin/$', views.SigninView, name="SigninView"),
    url(r'^signin/room/$', views.RoomView, name="RoomView"),
    url(r'^signin/room/add/', views.AddRoomView, name="AddRoomView"),
]
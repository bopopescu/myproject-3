from django.conf.urls import url
from cloudproject import views

app_name='cloudproject'

urlpatterns = [
    url(r'^$', views.HomePageView,name="HomePageView"),
    url(r'^signup/', views.SignupView , name="SignupView"),
    url(r'^signin/$', views.SigninView, name="SigninView"),
    url(r'^logout/', views.LogoutView, name="LogoutView"),
    url(r'^signin/room/$', views.RoomView, name="RoomView"),
    url(r'^signin/user/$', views.UserView, name="UserView"),
    url(r'^signin/user/booking/', views.BookRoomView, name="BookRoomView"),
    url(r'^signin/room/add/', views.AddRoomView, name="AddRoomView"),
    url(r'^signin/room/remove/', views.RemoveRoomView, name="RemoveRoomView"),
    url(r'^signin/room/update/', views.UpdatePriceView, name="UpdatePriceView"),
]
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('cloudproject.urls')),
    url(r'^signup/', include('cloudproject.urls')),
    url(r'^signin/', include('cloudproject.urls')),
]

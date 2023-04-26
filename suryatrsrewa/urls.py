from django.contrib import admin
from django.urls import path

from django.http import HttpResponse
import datetime


def index(request):
    now = datetime.datetime.now()
    html = "<html><body><h1>Suryabhan Kushwaha </h1></body></html>"
    return HttpResponse(html)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
]

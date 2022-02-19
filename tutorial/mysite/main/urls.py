from django.urls import path
from . import views # import views from the current directory


# this file gets the start part from home.
urlpatterns = [
    path("", views.index, name="index"),
    path("start/", views.start, name="index"), # 
    path("v1/", views.v1, name = "index")
]
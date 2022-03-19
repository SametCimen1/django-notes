from django.urls import path
from . import views # import views from the current directory



# this file gets the start part from home.
urlpatterns = [
    path("", views.home, name ="home"),
    path("<int:id>", views.list, name = "list")
]
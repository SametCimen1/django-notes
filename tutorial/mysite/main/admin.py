from django.contrib import admin
from . models import ToDoList, Item

# Register your models here.
# after you write the models 
admin.site.register(ToDoList)
admin.site.register(Item)
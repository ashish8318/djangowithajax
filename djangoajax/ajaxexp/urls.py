
from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name="home"),
    path('adduser',views.adduser,name="adduser"),
    path('delete',views.delete,name="delete"),
    path('edit',views.Edit,name="edit")
]
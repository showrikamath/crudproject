
from django.urls import path
from app import views

urlpatterns = [
    path('',views.index,name="index"),
    path('about',views.about,name="about"),
    path('insert',views.insertdata,name="insertdata"),
    path('update/<id>',views.updatedata,name="insertdata"),
    path('delete/<id>',views.deletedata,name="insertdata"),
]
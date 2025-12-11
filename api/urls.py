from django.urls import path
from . import views

urlpatterns =[
    #api endpoints
    path('v1/student/',views.studentView)
]
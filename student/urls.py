from django.urls import path
from . import views

urlpatterns =[
    #web app apis
    path('home/<int:pk>/',views.home),
#    path('stu-list/',views.students),

    #api endpoints
    # path('api/v1',views.students)
]


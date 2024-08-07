from django.urls import path
from . import views

urlpatterns =[
    path('<day>/<descreption>',views.dainamic_days),

    ]


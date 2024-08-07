from django.urls import path
from . import views


urlpatterns = [

   path('sunday', views.index),
   path('monday', views.index),
   path('edit', views.edit_profile),
]



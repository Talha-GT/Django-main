from django.urls import path
from . import views

urlpatterns = [
    path('buyer/',views.Buyer ),
    path('seller/',views.seller ),
    path('',views.home),
]

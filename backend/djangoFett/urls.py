from django.urls import path
from . import views

urlpatterns = [
    #splash page path
    path('', views.Home.as_view(), name="home")
]
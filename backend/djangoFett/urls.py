from django.urls import path
from . import views

urlpatterns = [
    #splash page path
    path('', views.Home.as_view(), name="home"),
    # auth signup path
    path('signup/', views.Signup.as_view(), name="signup"),
]
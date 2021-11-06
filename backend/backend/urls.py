from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #includes django-fett paths
    path('', include('djangoFett.urls')),
    #path for auth and login
    path('accounts/', include('django.contrib.auth.urls')),
]

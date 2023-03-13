from django.contrib import admin
from django.urls import path, include
from .views import hello_world
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_world),
    path('blog/', include('website.urls')),

] + 

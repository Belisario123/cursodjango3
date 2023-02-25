from django.contrib import admin
from django.urls import path
from views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_world())
]

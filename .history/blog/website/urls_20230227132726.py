from django.urls import path, include
from .views import hello_blog
from .views import post_deta


urlpatterns = [
    path('', hello_blog),
    path('post/<int:id>/', post_detail),


]

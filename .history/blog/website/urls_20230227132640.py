from django.urls import path, include
from .views import hello_blog


urlpatterns = [
    path('', hello_blog),
    path('post/<int:year>/', views.year_archive),


]

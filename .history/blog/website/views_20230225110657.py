from django.shortcuts import render

def hello_blog(request):
    lista = ['Django', 'Python', 'G']
    data = {'name': 'Curso de Django 3'}
    return render(request, 'index.html', data)
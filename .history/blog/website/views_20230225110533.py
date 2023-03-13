from django.shortcuts import render

def hello_blog(request):
    data = {'name': 'Curso de Django 3'}
    return render(request, 'indexgeral.html', data)
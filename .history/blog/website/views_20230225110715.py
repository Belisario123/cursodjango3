from django.shortcuts import render

def hello_blog(request):
    lista = ['Django', 'Python', 'Git', 'Html', 'Banco de dados', 'Linux']
    data = {'name': 'Curso de Django 3'}
    return render(request, 'index.html', data)
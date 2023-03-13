from django.shortcuts import render
from .models import Post

def hello_blog(request):
    lista = [
        'Django', 'Python', 'Git', 'Html', 
        'Banco de dados', 'Linux', 'Nginx', 'Uwsgi',
        'Systemctl'
    ]
    data = {'name': 'Curso de Django 3', 'lista_tecnologias': lista}

    list_posts = Post.
    return render(request, 'index.html', data,)
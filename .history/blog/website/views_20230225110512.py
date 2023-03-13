from django.shortcuts import render

def hello_blog(request):
    data = {'name': 'Curso de Djan'}
    return render(request, 'indexgeral.html')
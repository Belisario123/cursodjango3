from django.shortcuts import render

def hello_blog(request):
    data = {'name': 'Curso de '}
    return render(request, 'indexgeral.html')
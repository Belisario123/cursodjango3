from django.shortcuts import render

def hello_blog(request):
    data = {'name': 'Curso de D'}
    return render(request, 'indexgeral.html')
from django.shortcuts import render

def hello_blog(request):
    data = {'name': 'Curso de Django'}
    return render(request, 'indexgeral.html')
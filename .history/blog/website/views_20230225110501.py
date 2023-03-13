from django.shortcuts import render

def hello_blog(request):
    data = {'name'}
    return render(request, 'indexgeral.html')
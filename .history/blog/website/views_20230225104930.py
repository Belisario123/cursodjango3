from django.shortcuts import render

def hello_blog(request):
    return render(request, 'indexedu1.html')
from django.shortcuts import render

def hello_blog(request):
    return render(request, 'indexedu.html')
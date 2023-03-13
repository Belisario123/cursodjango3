from django.shortcuts import render

def hello_blog(request):
    return render(request, 'inde.html')
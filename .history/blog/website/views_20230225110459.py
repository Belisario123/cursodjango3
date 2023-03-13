from django.shortcuts import render

def hello_blog(request):
    data = {}
    return render(request, 'indexgeral.html')
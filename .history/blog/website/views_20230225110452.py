from django.shortcuts import render

def hello_blog(request):
    
    return render(request, 'indexgeral.html')
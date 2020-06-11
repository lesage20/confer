from django.shortcuts import render

# Create your views here.

def blog(request):
    datas = {
        
    }
    return render(request, 'blog.html', datas)

def detail(request):
    datas = {
        
    }
    return render(request, 'single-blog.html')
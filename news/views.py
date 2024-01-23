from django.shortcuts import render
from .models import Breaking_news

# Create your views here.
def home(request):
    breaking_news= Breaking_news.objects.all()
    context ={
        'breaking_news':breaking_news
    }
    return render(request, 'home.html', context)

def dashboard(request):
    return render(request, 'dashboard/index.html')



def slider(request):
    return render(request, 'dashboard/brakingnews/breaking.html')
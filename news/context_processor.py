from .models import Breaking_news
def get_all_breaking_news(request):
    breaking_news = Breaking_news.objects.all()
    context= {
        'breaking_news':breaking_news 
    }
    return context
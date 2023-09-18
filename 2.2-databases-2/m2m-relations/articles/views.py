from django.shortcuts import render

from .models import Article


def articles_list(request):
    template = 'articles/news.html'
    article_list = Article.objects.all()
    context = {
        'object_list': article_list
    }

    return render(request, template, context)

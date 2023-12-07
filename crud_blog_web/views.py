from .views.article_view import all_articles
from .views.article_view import test_response
from django.shortcuts import render
from django.http import HttpResponse
from .models import Article


# Create your views here.

def index(request):
    # return HttpResponse("Pierwszy widok")
    title_article = "Artykuły"
    articles = Article.objects.all()
    options = ["opcja 1", "opcja 2"]

    return render(request, template_name="articles.html",
                  context={
                      "title_article_view": title_article,
                      "options": options,
                      "articles": articles
                  })


def testORM(request):
    query = None
    return HttpResponse(query)


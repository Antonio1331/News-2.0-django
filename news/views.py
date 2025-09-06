from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from .models import Category, News, Comment
from .forms import CommentForm


def home(request: HttpRequest):
    newses = News.objects.all()
    categories = Category.objects.all()

    context = {
        "newses": newses,
        "categories": categories,
        "title": "Barcha maqolalar"
    }

    return render(request, "news/index.html", context)


def news_by_category(request, category_id: int):
    newses = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()

    context = {
        "newses": newses,
        "categories": categories,
        "title": Category.objects.get(pk=category_id).name
    }
    return render(request, "news/index.html", context)


def news_detail(request: HttpRequest, pk: int):
    categories = Category.objects.all()
    news = News.objects.get(pk=pk)

    news.views += 1
    news.save()

    context = {
        "news": news,
        "categories": categories,
        "title": news.title,
        'form': CommentForm()
    }
    return render(request, "news/news-detail.html", context)


def save_comment(request: HttpRequest, news_id: int):
    if request.method == "POST":
        form = CommentForm(data=request.POST)
        if form.is_valid():
            Comment.objects.create(
                text=request.POST.get("text"),
                news_id=news_id,
                user=request.user
            )
    return redirect("detail", pk=news_id)

from django.shortcuts import render

from django.template.response import TemplateResponse

from django.shortcuts import get_object_or_404
from .models import News, Item


def index(request):
    return TemplateResponse(
        request,
        "index.html",
        {"news_list": News.objects.all()[0:5], "item_list": Item.objects.all()},
    )


def news_detail(request, news_id):
    news = get_object_or_404(News, id=news_id)
    return TemplateResponse(request, "news_detail.html", {"news": news})


def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    return TemplateResponse(request, "item_detail.html", {"item": item})

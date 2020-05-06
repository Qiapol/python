import json
from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

import sys
sys.path.append('../')
from core.models import News, Item


@csrf_exempt
@require_http_methods(['GET', 'POST'])
def news_list(request):
    if request.method == 'GET':
        items = [news.to_dict() for news in News.objects.all()]
        return JsonResponse(items, safe=False)
    else: # POST
        params = json.loads(request.body)
        news = News.objects.create(
            day=datetime.strptime(params['day'], '%Y-%m-%d'),
            title=params['title'],
            body=params['body'],
        )
        return JsonResponse({'id': news.id})


@csrf_exempt
@require_http_methods(['GET', 'PUT', 'DELETE'])
def news_detail(request, news_id):
    if request.method == 'GET':
        news = get_object_or_404(News, id=news_id)
        return JsonResponse(news.to_dict())
    elif request.method == 'PUT':
        params = json.loads(request.body)
        News.objects.filter(id=news_id).update(
            day=datetime.strptime(params['day'], '%Y-%m-%d'),
            title=params['title'],
            body=params['body'],
        )
        return JsonResponse({})
    else: # DELETE
        News.objects.filter(id=news_id).delete()
        return JsonResponse({})


@csrf_exempt
@require_http_methods(['GET', 'POST'])
def item_list(request):
    if request.method == 'GET':
        items = [item.to_dict() for item in Item.objects.all()]
        return JsonResponse(items, safe=False)
    else: # POST
        params = json.loads(request.body)
        item = Item.objects.create(
            name=params['name'],
            price=params['price'],
            description=params['description'],
        )
        return JsonResponse({'id': item.id})


@csrf_exempt
@require_http_methods(['GET', 'PUT', 'DELETE'])
def item_detail(request, item_id):
    if request.method == 'GET':
        item = get_object_or_404(Item, id=item_id)
        return JsonResponse(item.to_dict())
    elif request.method == 'PUT':
        params = json.loads(request.body)
        Item.objects.filter(id=item_id).update(
            name=params['name'],
            price=params['price'],
            description=params['description'],
        )
        return JsonResponse({})
    else: # DELETE
        Item.objects.filter(id=item_id).delete()
        return JsonResponse({})

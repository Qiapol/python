import json
from datetime import datetime

from django.db import transaction
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Customer, CustomerLog
from .forms import RegisterCustomerAPIForm, RegisterCustomerAndLogAPIForm

# 今回は静的トークンを実装
API_TOKEN = "dkwRNwBXq8HauWWUBesZBiuctRDBBJRneHNLzaBj4CAhZQrE"


def token_required(func):
    """
    APIトークンの確認デコレータを実装
    :param func:
    :return:
    """
    def _wrapped(request, *args, **kwargs):
        if 'token' not in request.GET or request.GET['token'] != API_TOKEN:
            return JsonResponse({}, status=403)
        return func(request, *args, **kwargs)
    return _wrapped


# @token_required
def customer_list(request):
    return JsonResponse([customer.to_dict() for customer in Customer.objects.all()], safe=False)


# @token_required
def customer_and_log(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    logs = CustomerLog.objects.filter(customer_id=customer.id)

    res = customer.to_dict()
    res['logs'] = [log.to_dict() for log in logs]
    return JsonResponse(res)


# @token_required
def search_customer(request):
    # GETのAPIの場合、パラメータはrequest.GET.get()で取り出す
    keyword = request.GET.get('keyword')
    if not keyword:
        return JsonResponse([], safe=False)
    customer_list = [
        customer.to_dict()
        for customer in Customer.objects.filter(
            Q(name__contains=keyword) | Q(email__contains=keyword)
        )
    ]
    return JsonResponse(customer_list, safe=False)


# @token_required
def _convert_str_to_date(yyyymmdd):
    return datetime.strptime(yyyymmdd, '%Y-%m-%d').date()


# @token_required
def filter_logs(request):
    from_ = _convert_str_to_date(request.GET['from'])
    to_ = _convert_str_to_date(request.GET['to'])

    logs = CustomerLog.objects.filter(created_at__gte=from_, created_at__lte=to_).order_by(
        'created_at'
    )
    return JsonResponse([log.to_dict(include_customer_id=True) for log in logs], safe=False)


# @token_required
@csrf_exempt
def register_customer(request):
    form = RegisterCustomerAPIForm(json.loads(request.body))
    if not form.is_valid():
        return JsonResponse({'code': 'invalid_request'}, status=400)
    form.save()
    return JsonResponse({})


@csrf_exempt
@transaction.atomic()
def register_customer_and_log(request):
    data = json.loads(request.body)
    form = RegisterCustomerAPIForm(data)
    if not form.is_valid():
        return JsonResponse({'code': 'invalid_request'}, status=400)

    customer = form.save()
    CustomerLog.objects.create(
        customer=customer, amount=form.cleaned_data['amount'], note=form.cleaned_data['note']
    )
    return JsonResponse({})

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import  Http404, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from .forms import ProductSearchForm, ProductEditFrom
from .models import Product


def product_list(request):
    # Productのデータ一覧を取得
    products = Product.objects.order_by('name')

    # 検索機能の追加
    form = ProductSearchForm(request.GET)
    products = form.filter_product(products)

    # request.GETの内容をコピーし、'page'以外のパラメータを引き継げるようにする
    # 本実装理由は、ページ移動の際に検索条件を引き継げるようにするためである
    params = request.GET.copy()
    if 'page' in params:
        page = params['page']
        del params['page']
    # 今までの処理(page = request.GET.get('page', 1))はココ
    else:
        page = 1
    search_params = params.urlencode()

    paginator = Paginator(products, 5)

    try:
        products = paginator.page(page)
    except (EmptyPage, PageNotAnInteger):
        products = paginator.page(1)

    return TemplateResponse(request, 'catalogue/product_list.html',
                            {'products': products,
                             'form': form,
                             'search_params': search_params})


def product_detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        raise Http404
    return TemplateResponse(request, 'catalogue/product_detail.html',
                            {'product': product})


def product_edit(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        raise Http404

    if request.method == 'POST':
        form = ProductEditFrom(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('product_detail', args=(product.id,)))
    else:
        form = ProductEditFrom(instance=product)
    return TemplateResponse(request, 'catalogue/product_edit.html',
                            {'form': form, 'product': product})


# @require_POST
@require_http_methods(["GET", "POST"])
def product_delete(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        raise Http404

    if request.method == 'POST':
        product.delete()
        return HttpResponseRedirect(reverse('product_list'))
    else:
        return TemplateResponse(request, 'catalogue/product_delete.html',
                                {'product': product})

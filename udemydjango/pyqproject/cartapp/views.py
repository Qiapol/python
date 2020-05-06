from django.http import HttpResponseRedirect, Http404
from django.template.response import TemplateResponse
from django.urls import reverse
from django.views.decorators.http import require_POST

# 応急処置。cartappがルートになっているために、普通に書くとcatalogueapp内のモジュールアクセスができない。
# Pythonの特性で、実行モジュールのあるディレクトリがルートディレクトリになるルールがある：つまり上の階層には行けない
import sys
sys.path.append('../')
from catalogueapp.models import Product


@require_POST
def cart_add(request, product_id):
    # Product(model)に無いproduct_idが指定された場合に404エラーを出力
    if not Product.objects.filter(id=product_id).exists():
        raise Http404

    # Sessionからcartを取り出す
    cart = request.session.get('cart')
    if cart:
        # cartが存在するなら追加して、新しいcartに更新する{'cart': cart}
        cart.append(product_id)
        request.session['cart'] = cart
    else:
        # 無いなら新しく'cart'を作成する
        # sessionオブジェクトにcart要素を追加するイメージ
        request.session['cart'] = [product_id]
    return HttpResponseRedirect(reverse('product_list'))


def cart_list(request):
    cart = request.session.get('cart')
    if cart:
        products = []
        for product_id in cart:
            try:
                product = Product.objects.get(id=product_id)
                products.append(product)
            except Product.DoesNotExist:
                pass
    else:
        products = []

    total_price = 0
    for product in products:
        total_price += product.price

    return TemplateResponse(request, 'cart/list.html',
                            {'products': products,
                             'total_price': total_price})


@require_POST
def cart_delete(request, product_id):
    cart = request.session.get('cart')
    if cart:
        filtered = []
        for p in cart:
            if p != product_id:
                filtered.append(p)
        request.session['cart'] = filtered
    return HttpResponseRedirect(reverse('cart_list'))

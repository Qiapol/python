from django import forms
from .models import Product


class ProductSearchForm(forms.ModelForm):
    # Produce(model)に加えて使用したい項目をここに記載する
    # その他、Produce(model)にあるのにココに記載するのは、required=Falseにしたいなどの意図あり
    name = forms.CharField(label='商品名', required=False)
    price_min = forms.IntegerField(label='最低価格', required=False)
    price_max = forms.IntegerField(label='最高価格', required=False)

    # 項目：categoryに関しては、Product(model)から取得される
    class Meta:
        model = Product
        fields = {
            'category',
        }

    def filter_product(self, products):
        """
        入力された検索条件でproductsをfilterする
        :param products:
        :return products:
        """
        # バリデーションエラーの場合は、productsをそのまま返す
        if not self.is_valid():
            return products

        # cleaned_dataを使用することで、バリデーション済のフォームの値を辞書形式で取得できる
        name = self.cleaned_data.get('name')
        price_min = self.cleaned_data.get('price_min')
        price_max = self.cleaned_data.get('price_max')
        category_id = self.cleaned_data.get('category')
        # products(Products(model))のデータ一覧からfilterをかけていく
        # この時、Djangoのルックアップという仕組みを使用している

        # __contains: name(文字列等)が含まれているか、検索できる
        if name:
            products = products.filter(name__contains=name)
        # __gte(greater than or equal to) = '>='(以上)
        if price_min:
            products = products.filter(price__gte=price_min)
        # __lte(lower than or equal to) = '<='(以下)
        if price_max:
            products = products.filter(price__lte=price_max)
        if category_id:
            products = products.filter(category_id=category_id)
        return products


class ProductEditFrom(forms.ModelForm):

    class Meta:
        model = Product
        fields = {'name', 'price'}

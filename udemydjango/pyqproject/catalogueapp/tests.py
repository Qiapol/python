from django.test import TestCase
from django.urls import reverse

from .forms import ProductSearchForm
from .models import Category, Product


class TestProductList(TestCase):

    def test_get(self):
        category = Category.objects.create(name='カテゴリー1')
        Product.objects.create(name='test1', price=100, category=category)
        Product.objects.create(name='test2', price=200, category=category)

        res = self.client.get(reverse('product_list'))
        self.assertTemplateUsed(res, 'catalogue/product_list.html')
        self.assertContains(res, 'test1')
        self.assertContains(res, '100円')
        self.assertContains(res, 'test2')
        self.assertContains(res, '200円')
        self.assertContains(res, 'カテゴリー1')


class TestProductDetail(TestCase):
    def test_get(self):
        Product.objects.create(id=1, name='test1', price=100)
        res = self.client.get(reverse('product_detail', args=(1,)))
        self.assertTemplateUsed(res, 'catalogue/product_detail.html')
        self.assertContains(res, 'test1')
        self.assertContains(res, '100円')

    def test_404(self):
        res = self.client.get(reverse('product_detail', args=(1,)))
        self.assertEqual(res.status_code, 404)


class TestProductEdit(TestCase):
    def test_get(self):
        product = Product.objects.create(id=1, name='test1', price=100)
        res = self.client.get(reverse('product_edit', args=(1,)))
        # ResponseObjectにおいて、指定したテンプレートが使用されているか
        self.assertTemplateUsed(res, 'catalogue/product_edit.html')
        # TemplateResponseで指定したデータが正しく送られているか
        # res.context['form'].instanceの値は、formのinstance属性で指定したもの。
        self.assertEqual(res.context['form'].instance, product)
        self.assertEqual(res.context['product'], product)

    def test_post(self):
        product = Product.objects.create(id=1, name='test1', price=100)
        res = self.client.post(reverse('product_edit', args=(1,)),
                               data={'name': '変更', 'price': 200})
        self.assertRedirects(res, reverse('product_detail', args=(product.id,)))
        # DBの値がテストによって変更されているので、再読込を行っている
        product.refresh_from_db()
        self.assertEqual(product.name, '変更')
        self.assertEqual(product.price, 200)

    def test_post_invalid(self):
        product = Product.objects.create(id=1, name='test1', price=200)
        # 無効な値を記入
        res = self.client.post(reverse('product_edit', args=(1,)),
                               data={'name': ''})
        self.assertTemplateUsed(res, 'catalogue/product_edit.html')
        self.assertFalse(res.context['form'].is_valid())
        self.assertEqual(res.context['form'].instance, product)
        self.assertEqual(res.context['product'], product)

    def test_404(self):
        res = self.client.post(reverse('product_edit', args=(1,)), data={'name': 'テスト'})
        self.assertEqual(res.status_code, 404)


class TestProductDelete(TestCase):
    def test_get(self):
        product = Product.objects.create(id=1, name='test1', price=100)
        res = self.client.get(reverse('product_delete', args=(1,)))
        self.assertTemplateUsed(res, 'catalogue/product_delete.html')
        self.assertEqual(res.context['product'], product)

    def test_post(self):
        product = Product.objects.create(id=1, name='test1', price=100)
        res = self.client.post(reverse('product_delete', args=(1,)))
        self.assertRedirects(res, reverse('product_list'))
        self.assertFalse(Product.objects.exists())

    def test_404(self):
        res = self.client.get(reverse('product_delete', args=(1,)))
        self.assertEqual(res.status_code, 404)


class TestProductSearchForm(TestCase):
    def test_filter_products_name(self):
        Product.objects.create(name='冷凍パスタ', price=800)
        Product.objects.create(name='冷凍餃子', price=100)
        Product.objects.create(name='煮込みグラタン', price=700)

        form = ProductSearchForm({'name': '冷凍'})
        actual = form.filter_product(Product.objects.order_by('name'))
        self.assertEqual(len(actual), 2)
        self.assertEqual(actual[0].name, '冷凍パスタ')
        self.assertEqual(actual[1].name, '冷凍餃子')

    def test_filter_products_price_min(self):
        Product.objects.create(name='冷凍グラタン', price=699)
        Product.objects.create(name='煮込みグラタン', price=700)

        form = ProductSearchForm({'price_min': 700})
        actual = form.filter_product(Product.objects.all())
        self.assertEqual(len(actual), 1)
        self.assertEqual(actual[0].name, '煮込みグラタン')

    def test_filter_products_price_max(self):
        Product.objects.create(name='煮込みグラタン', price=700)
        Product.objects.create(name='ドリア', price=701)

        form = ProductSearchForm({'price_max': 700})
        actual = form.filter_product(Product.objects.all())
        self.assertEqual(len(actual), 1)
        self.assertEqual(actual[0].name, '煮込みグラタン')

    def test_filter_products_category(self):
        category = Category.objects.create(id=1, name='食品')
        Product.objects.create(name='煮込みグラタン', price=700, category=category)
        Product.objects.create(name='おしゃれスカジャン', price=8900)

        form = ProductSearchForm({'category': 1})
        actual = form.filter_product(Product.objects.all())
        self.assertEqual(len(actual), 1)
        self.assertEqual(actual[0].name, '煮込みグラタン')

    def test_filter_invalid(self):
        Product.objects.create(name='おしゃれスカジャン', price=8900)
        Product.objects.create(name='煮込みグラタン', price=700)

        form = ProductSearchForm({'price_min': 'invalid'})
        actual = form.filter_product(Product.objects.all())
        self.assertEqual(len(actual), 2)
        self.assertEqual(actual[0].name, 'おしゃれスカジャン')
        self.assertEqual(actual[1].name, '煮込みグラタン')

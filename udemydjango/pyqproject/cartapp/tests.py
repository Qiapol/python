from django.test import TestCase
from django.urls import reverse

import sys
sys.path.append('../')
from catalogueapp.models import Product


class TestCartList(TestCase):
    def test_get(self):
        Product.objects.create(id=1, name='test1', price=100)
        Product.objects.create(id=2, name='test2', price=200)
        session = self.client.session
        session['cart'] = [1, 2]
        session.save()

        res = self.client.get(reverse('cart_list'))
        self.assertTemplateUsed(res, 'cart/list.html')
        self.assertContains(res, 'test1: 100円')
        self.assertContains(res, 'test2: 200円')
        self.assertContains(res, '合計金額: 300円')

    def test_get_product_not_exist(self):
        session = self.client.session
        session['cart'] = [1]
        session.save()

        res = self.client.get(reverse('cart_list'))
        self.assertContains(res, '合計金額: 0円')

    def test_get_cart_empty(self):
        res = self.client.get(reverse('cart_list'))
        self.assertContains(res, '合計金額: 0円')


class TestCartAdd(TestCase):
    def test_session_not_exists_add_cart(self):
        Product.objects.create(id=1, name='test1', price=100)
        res = self.client.post(reverse('cart_add', args=(1,)))
        self.assertRedirects(res, reverse('product_list'))
        self.assertEqual(self.client.session['cart'], [1])

    def test_session_exist_add_cart(self):
        Product.objects.create(id=1, name='test1', price=100)
        Product.objects.create(id=2, name='test2', price=200)
        session = self.client.session
        session['cart'] = [1]
        session.save()

        res = self.client.post(reverse('cart_add', args=(2,)))
        self.assertRedirects(res, reverse('product_list'))
        self.assertEqual(self.client.session['cart'], [1, 2])

    def test_get_product_not_exist(self):
        res = self.client.post(reverse('cart_add', args=(1,)))
        self.assertEqual(res.status_code, 404)

    def test_not_post_method(self):
        res = self.client.get(reverse('cart_add', args=(1,)))
        self.assertEqual(res.status_code, 405)


class TestCartDelete(TestCase):
    def test_product_delete(self):
        Product.objects.create(id=1, name='test1', price=100)
        Product.objects.create(id=2, name='test2', price=200)
        session = self.client.session
        session['cart'] = [1, 2]
        session.save()

        res = self.client.post(reverse('cart_delete', args=(1,)))
        self.assertRedirects(res, reverse('cart_list'))
        self.assertEqual(self.client.session['cart'], [2])

    def test_not_exist_product_delete(self):
        res = self.client.post(reverse('cart_delete', args=(1,)))
        self.assertRedirects(res, reverse('cart_list'))
        self.assertNotIn('cart', self.client.session)

        # Product.objects.create(id=1, name='test1', price=100)
        # session = self.client.session
        # session['cart'] = [1]
        # session.save()
        #
        # res = self.client.post(reverse('cart_delete', args=(2,)))
        # self.assertRedirects(res, reverse('cart_list'))
        # self.assertEqual(self.client.session['cart'], [1])

    def test_not_post_method(self):
        res = self.client.get(reverse('cart_delete', args=(1,)))
        self.assertEqual(res.status_code, 405)

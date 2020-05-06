import json
from django.test import TestCase
from datetime import date

import sys
sys.path.append('../')
from core.models import News, Item

class TestViews(TestCase):
    def test1(self):
        News.objects.create(id=1, day=date(2017, 8, 1), title="title1", body="body1")
        News.objects.create(id=2, day=date(2017, 8, 2), title="title2", body="body2")

        res = self.client.get("/api/news/")
        news_list = res.json()
        self.assertEqual(len(news_list), 2, msg="プログラムが期待する動作と違いました。確認してください。")
        news2 = news_list[0]
        self.assertEqual(news2["id"], 2)
        self.assertEqual(news2["day"], "2017-08-02")
        self.assertEqual(news2["title"], "title2")
        self.assertEqual(news2["body"], "body2")

        news1 = news_list[1]
        self.assertEqual(news1["id"], 1)
        self.assertEqual(news1["day"], "2017-08-01")
        self.assertEqual(news1["title"], "title1")
        self.assertEqual(news1["body"], "body1")

    def test2(self):
        News.objects.create(id=1, day=date(2017, 8, 1), title="title1", body="body1")
        News.objects.create(id=2, day=date(2017, 8, 2), title="title2", body="body2")

        res = self.client.get("/api/news/1")
        news1 = res.json()
        self.assertEqual(news1["id"], 1)
        self.assertEqual(news1["day"], "2017-08-01")
        self.assertEqual(news1["title"], "title1")
        self.assertEqual(news1["body"], "body1")

    def test3(self):
        Item.objects.create(id=1, name="item1", price=1, description="description1")
        Item.objects.create(id=2, name="item2", price=2, description="description2")

        res = self.client.get("/api/items/")
        item_list = res.json()
        self.assertEqual(len(item_list), 2, msg="プログラムが期待する動作と違いました。確認してください。")

        item1 = item_list[0]
        self.assertEqual(item1["id"], 1)
        self.assertEqual(item1["name"], "item1")
        self.assertEqual(item1["price"], 1)
        self.assertEqual(item1["description"], "description1")

        item2 = item_list[1]
        self.assertEqual(item2["id"], 2)
        self.assertEqual(item2["name"], "item2")
        self.assertEqual(item2["price"], 2)
        self.assertEqual(item2["description"], "description2")

    def test4(self):
        Item.objects.create(id=1, name="item1", price=1, description="description1")
        Item.objects.create(id=2, name="item2", price=2, description="description2")

        res = self.client.get("/api/items/1")
        item = res.json()
        self.assertEqual(item["id"], 1)
        self.assertEqual(item["name"], "item1")
        self.assertEqual(item["price"], 1)
        self.assertEqual(item["description"], "description1")

    def test5(self):
        params = {"day": "2017-08-01", "title": "title1", "body": "body1"}
        res = self.client.post("/api/news/", json.dumps(params), content_type="application/json")
        self.assertEqual(res.status_code, 200)

        news = News.objects.get()
        self.assertEqual(news.day, date(2017, 8, 1))
        self.assertEqual(news.title, "title1")
        self.assertEqual(news.body, "body1")

    def test6(self):
        News.objects.create(id=1, day=date(2017, 8, 1), title="title1", body="body1")
        params = {"day": "2017-08-02", "title": "title2", "body": "body2"}
        res = self.client.put("/api/news/1", json.dumps(params), content_type="application/json")
        self.assertEqual(res.status_code, 200)

        news = News.objects.get()
        self.assertEqual(news.day, date(2017, 8, 2))
        self.assertEqual(news.title, "title2")
        self.assertEqual(news.body, "body2")

    def test7(self):
        News.objects.create(id=1, day=date(2017, 8, 1), title="title1", body="body1")
        res = self.client.delete("/api/news/1", content_type="application/json")
        self.assertEqual(res.status_code, 200)

        self.assertEqual(News.objects.count(), 0)

    def test8(self):
        # 登録テスト
        params = {"name": "name1", "price": 1, "description": "description1"}
        res = self.client.post("/api/items/", json.dumps(params), content_type="application/json")
        self.assertEqual(res.status_code, 200)
        item = Item.objects.get()
        self.assertEqual(item.name, params["name"])
        self.assertEqual(item.price, params["price"])
        self.assertEqual(item.description, params["description"])
        Item.objects.all().delete()

        # 更新テスト
        Item.objects.create(id=1, name="item1", price=1, description="description1")
        params = {"name": "name2", "price": 2, "description": "description2"}
        res = self.client.put("/api/items/1", json.dumps(params), content_type="application/json")
        self.assertEqual(res.status_code, 200)
        item = Item.objects.get()
        self.assertEqual(item.name, params["name"])
        self.assertEqual(item.price, params["price"])
        self.assertEqual(item.description, params["description"])
        Item.objects.all().delete()

        # 削除テスト
        Item.objects.create(id=1, name="item1", price=1, description="description1")
        res = self.client.delete("/api/items/1", content_type="application/json")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(Item.objects.count(), 0)
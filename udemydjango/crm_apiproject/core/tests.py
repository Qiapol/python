import json
from datetime import date
from django.test import TestCase
from .models import Customer, CustomerLog


class TestViews(TestCase):
    def test0(self):
        Customer.objects.create(name="name1", age=1, email="shin+1@example.com")
        Customer.objects.create(name="name1", age=2, email="shin+2@example.com")

        res = self.client.get("/api/customer/")
        news_list = res.json()
        self.assertEqual(len(news_list), 2, msg="プログラムが期待する動作と違いました。確認してください。")

    def test1(self):
        Customer.objects.create(id=1, name="name1", age=1, email="shin+1@example.com")
        Customer.objects.create(id=2, name="name2", age=2, email="shin+2@example.com")
        CustomerLog.objects.create(customer_id=1, amount=1, note="1")
        CustomerLog.objects.create(customer_id=1, amount=2, note="2")
        CustomerLog.objects.create(customer_id=2, amount=3, note="3")

        res = self.client.get("/api/customer/1/logs")
        self.assertEqual(res.status_code, 200)
        customer = res.json()
        self.assertEqual(customer["name"], "name1")
        self.assertEqual(customer["email"], "shin+1@example.com")
        self.assertEqual(customer["age"], 1)

        logs = customer["logs"]
        self.assertEqual(len(logs), 2)

        log2 = logs[0]
        self.assertEqual(log2["amount"], 2)
        self.assertEqual(log2["note"], "2")

        log1 = logs[1]
        self.assertEqual(log1["amount"], 1)
        self.assertEqual(log1["note"], "1")

    def test2(self):
        Customer.objects.create(id=1, name="hanako yamada", age=1, email="shin+1@example.com")
        Customer.objects.create(id=2, name="taro yamada", age=2, email="shin+2@example.com")

        res = self.client.get("/api/customer/search?keyword=shin")
        customer_list = res.json()
        self.assertEqual(len(customer_list), 2)

        res = self.client.get("/api/customer/search?keyword=taro")
        customer_list = res.json()
        self.assertEqual(len(customer_list), 1)
        customer = customer_list[0]
        self.assertEqual(customer["name"], "taro yamada")
        self.assertEqual(customer["age"], 2)

    def test3(self):
        Customer.objects.create(id=1, name="name1", age=1, email="shin+1@example.com")
        Customer.objects.create(id=2, name="name2", age=2, email="shin+2@example.com")
        CustomerLog.objects.create(customer_id=1, amount=1, note="1", created_at=date(2017, 7, 21))
        CustomerLog.objects.create(customer_id=1, amount=2, note="2", created_at=date(2017, 7, 25))
        CustomerLog.objects.create(customer_id=2, amount=3, note="3", created_at=date(2017, 8, 1))

        res = self.client.get("/api/customer/filter_logs?from=2017-7-21&to=2017-7-25")
        logs = res.json()
        self.assertEqual(len(logs), 2)

        log1 = logs[0]
        self.assertEqual(log1["customer_id"], 1)
        self.assertEqual(log1["note"], "1")
        log2 = logs[1]
        self.assertEqual(log2["customer_id"], 1)
        self.assertEqual(log2["note"], "2")

        res = self.client.get("/api/customer/filter_logs?from=2017-8-1&to=2017-8-1")
        logs = res.json()
        self.assertEqual(len(logs), 1)
        log1 = logs[0]
        self.assertEqual(log1["customer_id"], 2)
        self.assertEqual(log1["note"], "3")

    def test4(self):
        Customer.objects.create(id=1, name="name1", age=1, email="shin+1@example.com")
        res = self.client.get("/api/customer/?token=invalid")
        self.assertEqual(res.status_code, 403)

        res = self.client.get(
            "/api/customer/?token=dkwRNwBXq8HauWWUBesZBiuctRDBBJRneHNLzaBj4CAhZQrE"
        )
        self.assertEqual(res.status_code, 200)
        customer_list = res.json()
        self.assertEqual(customer_list[0]["name"], "name1")

    def test5(self):
        res = self.client.post(
            "/api/customer/register", json.dumps({}), content_type="application/json"
        )
        self.assertEqual(res.status_code, 400)
        error = res.json()
        self.assertEqual(error, {"code": "invalid_request"})

        res = self.client.post(
            "/api/customer/register",
            json.dumps({"name": "taro yamada", "email": "shin1@example.com"}),
            content_type="application/json",
        )
        self.assertEqual(res.status_code, 400)
        error = res.json()
        self.assertEqual(error, {"code": "invalid_request"})

        res = self.client.post(
            "/api/customer/register",
            json.dumps({"name": "taro yamada", "email": "shin1@example.com", "age": 20}),
            content_type="application/json",
        )
        self.assertEqual(res.status_code, 200)
        self.assertEqual(Customer.objects.count(), 1)

    def test6(self):
        res = self.client.post(
            "/api/customer/register_and_log",
            json.dumps({"name": "taro yamada"}),
            content_type="application/json",
        )
        self.assertEqual(res.status_code, 400)
        error = res.json()
        self.assertEqual(error, {"code": "invalid_request"})

        res = self.client.post(
            "/api/customer/register_and_log",
            json.dumps(
                {
                    "name": "taro yamada",
                    "email": "shin1@example.com",
                    "age": 20,
                    "note": "aa",
                    "amount": "not int",
                }
            ),
            content_type="application/json",
        )
        self.assertEqual(res.status_code, 400)
        error = res.json()
        self.assertEqual(error, {"code": "invalid_request"})

        res = self.client.post(
            "/api/customer/register_and_log",
            json.dumps(
                {
                    "name": "taro yamada",
                    "email": "shin1@example.com",
                    "age": 20,
                    "note": "aa",
                    "amount": 100,
                }
            ),
            content_type="application/json",
        )
        self.assertEqual(res.status_code, 200)


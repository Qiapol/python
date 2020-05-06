from datetime import datetime
from django.db import models


class Customer(models.Model):
    """ 顧客
    """

    name = models.CharField("氏名", max_length=64)
    email = models.EmailField("メールアドレス")
    age = models.IntegerField("年齢")
    created_at = models.DateTimeField("登録日時", default=datetime.now)

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "age": self.age,
            "created_at": f"{self.created_at:%Y-%m-%d %H:%M:%S}",
        }

    class Meta:
        db_table = "customer"
        ordering = ("-id",)


class CustomerLog(models.Model):
    """ 顧客来店記録
        顧客が来店する度に、いついくら利用したかを記録するテーブル
    """

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    amount = models.IntegerField("支払い金額")
    note = models.TextField("メモ", null=True, blank=True)  # 任意
    created_at = models.DateTimeField("来店日時", default=datetime.now)

    def to_dict(self, include_customer_id=False):
        tmp = {
            'amount': self.amount,
            'note': self.note,
            'created_at': f"{self.created_at:%Y-%m-%d %H:%M:%S}",
        }
        if include_customer_id:
            tmp['customer_id'] = self.customer_id
        return tmp

    class Meta:
        db_table = "customer_log"
        ordering = ("-created_at",)

from django.db import models


class News(models.Model):
    """ お知らせ（新着情報）
        サイトへ訪れた人向けの新着情報を保持するモデル
    """

    day = models.DateField("日")
    title = models.CharField("タイトル", max_length=128)
    body = models.TextField("内容")

    # to_dict method をmodelに持たせた理由
    # ユニットテストをやりやすくするため(view内で記載すると、これが難しくなる)
    # 別のview関数でも共通処理として使用しやすくなる
    def to_dict(self):
        return {
            'id': self.id,
            'day': f'{self.day:%Y-%m-%d}',
            'title': self.title,
            'body': self.body,
        }

    class Meta:
        db_table = "news"
        ordering = ("-day",)


class Item(models.Model):
    """ 商品
    """

    name = models.CharField("商品名", max_length=128)
    description = models.TextField("商品説明")
    price = models.PositiveIntegerField("価格")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
        }

    class Meta:
        db_table = "item"


from django.db import models
from django.utils import timezone


class Vegetable(models.Model):

    """野菜."""

    name = models.CharField('名前', max_length=100)
    price = models.IntegerField('値段', default=0)
    description = models.TextField('説明')
    producer = models.CharField('生産者', max_length=50, default='ウメ')
    sold_out = models.BooleanField('売り切れ', help_text='売り切れの場合True', default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'vegetable'
        verbose_name = verbose_name_plural = '野菜'


class Comment(models.Model):

    """感想."""

    name = models.CharField('名前', max_length=50)
    message = models.CharField('メッセージ', max_length=200)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'comment'
        verbose_name = verbose_name_plural = '感想'


class Good(models.Model):

    """いいね."""

    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'good'
        verbose_name = verbose_name_plural = 'いいね'

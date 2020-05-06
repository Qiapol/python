# Generated by Django 3.0.5 on 2020-05-03 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='商品名')),
                ('description', models.TextField(verbose_name='商品説明')),
                ('price', models.PositiveIntegerField(verbose_name='価格')),
            ],
            options={
                'db_table': 'item',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(verbose_name='日')),
                ('title', models.CharField(max_length=128, verbose_name='タイトル')),
                ('body', models.TextField(verbose_name='内容')),
            ],
            options={
                'db_table': 'news',
                'ordering': ('-day',),
            },
        ),
    ]
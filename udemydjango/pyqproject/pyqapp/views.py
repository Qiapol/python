from random import choice

from django.shortcuts import redirect
from django.template.response import TemplateResponse
from .forms import CommentForm
from .models import Comment, Vegetable, Good

name = 'ウメ'
sub_titles = ['美味しいよ！', 'お買い得！', '産地直送！', 'とれたてをお届け！']


def index(request):
    """メイン画面."""
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            # データの新規追加
            form.save()
    else:
        # 入力用フォーム
        form = CommentForm()

    # タイトルを作成
    title = name + 'の野菜販売'

    # サブタイトルを決定
    sub_title = choice(sub_titles)

    # 野菜一覧
    vegetables = Vegetable.objects.filter(producer='ウメ').order_by('price')

    # コメント
    comments = Comment.objects.order_by('-created_at')[:3]

    # いいねの数
    good_count = Good.objects.count()

    return TemplateResponse(request, 'garden/index.html',
                            {'title': title,
                             'sub_title': sub_title,
                             'vegetables': vegetables,
                             'form': form,
                             'comments': comments,
                             'good_count': good_count})


def good(request):
    """いいねボタンをクリック"""
    if request.method == 'POST':
        # データの新規追加
        Good.objects.create()

    return redirect('index')

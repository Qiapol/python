from django.template.response import TemplateResponse
from .models import Vegetable, Comment
from .forms import CommentForm
import random

name = 'ウメ'
sub_titles = ['美味しいよ！', 'お買い得！', '産地直送！', 'とれたてをお届け！']
message = 'indexに入っていません'


def index(request):
    """メイン画面"""
    message = None
    if request.method == 'POST':
        message = 'POSTメソッドに入っています'
        form = CommentForm(request.POST)
        if form.is_valid():
            # データの新規追加
            form.save()
    else:
        # 入力用フォーム
        message = 'POSTメソッドに入っていません'
        form = CommentForm()

    # タイトルの作成
    title = name + 'の野菜販売'
    # サブタイトルの決定
    sub_title = random.choice(sub_titles)
    # model.Vegetableからデータ取得
    vegetables = Vegetable.objects.filter(producer='ウメ').order_by('price')
    # コメント
    comments = Comment.objects.order_by('-created_at')[:3]

    return TemplateResponse(request, 'garden/index.html',
                            {'title': title, 'sub_title': sub_title, 'vegetables': vegetables,
                             'form': form, 'comments': comments })

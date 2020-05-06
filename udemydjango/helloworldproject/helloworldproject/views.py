from django.http import HttpResponse
from typing import Any

from django.views.generic import TemplateView


def helloworldfunction(request: Any) -> HttpResponse:
    return HttpResponse('<h1>hello world</h1>')

class HelloWorldView(TemplateView):
    # どのテンプレート(htmlファイル)を基にページ作成を行うか
    template_name = 'hello.html'

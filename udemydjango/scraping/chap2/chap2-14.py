import requests
from bs4 import BeautifulSoup
from pathlib import Path
import urllib
import time

# Webページを取得して解析する
load_url = 'https://www.ymori.com/books/python2nen/test2.html'
html = requests.get(load_url)
soup = BeautifulSoup(html.content, 'html.parser')

# 保存用フォルダの作成
out_folder = Path('download2')
out_folder.mkdir(exist_ok=True)

print(out_folder)

# すべてのimgタグを検索し、リンクを更新する(相対パスは絶対パスへ)
for element in soup.find_all('img'):
    src = element.get('src')

    # 絶対パスに変換し、画像ファイルを取得
    image_url = urllib.parse.urljoin(load_url, src)
    imgdata = requests.get(image_url)

    # URLから最後のファイル名を取り出して、ディレクトリパス + ファイル名をつけ保存先Pathを完成させる
    filename = image_url.split('/')[-1]
    out_path = out_folder.joinpath(filename)

    # 画像データをファイルに書き出す
    with open(out_path, 'wb') as f:
        f.write(imgdata.content)


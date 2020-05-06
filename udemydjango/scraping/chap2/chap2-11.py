import requests

# 画像ファイルを取得する
image_url = 'https://www.ymori.com/books/python2nen/sample1.png'
imgdata = requests.get(image_url)

# URLから最後のファイル名を取り出す
filename = image_url.split('/')[-1]

# 画像データをファイルに書き出す(モードは画像データよりバイナリで行う)
with open(filename, 'wb') as f:
    f.write(imgdata.content)

print('-------------------------------------------')
# split()の挙動を確認
s = 'a/b/c/d/e'
print(s.split('/'))
print(s.split('/')[-1])

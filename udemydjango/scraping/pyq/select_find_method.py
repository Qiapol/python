import requests
from bs4 import BeautifulSoup

# Webページを取得して解析する
load_url = 'https://www.ymori.com/books/python2nen/test2.html'
html = requests.get(load_url)
soup = BeautifulSoup(html.content, 'html.parser')

# 検証(find, select)
print('find method')
chap2_find = soup.find(id='chap2')
print(chap2_find)
print(chap2_find.text)

print('------------------------------------')
print('select method')
# またはsoup.select('#chap2')[0]でもOK。indexが無いとエラー発生
# select methodはlistで返すので、indexが必要になってくる
chap2_select = soup.select_one('#chap2')
print(chap2_select)
print(chap2_select.text)

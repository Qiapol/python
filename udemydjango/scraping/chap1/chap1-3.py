import requests

url = 'https://www.ymori.com/books/python2nen/test1.html'
response = requests.get(url)

response.encoding = response.apparent_encoding

filename = 'download.txt'
with open(filename, 'w', encoding='utf-8') as f:
    f.write(response.text)

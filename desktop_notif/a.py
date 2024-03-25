import requests as r
url='https://raw.githubusercontent.com/th3x3rx3s/Python/master/test.json'
url=r.get(url)
print(url.json()['coord']['lat'])
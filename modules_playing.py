import urllib.request
response = urllib.request.urlopen("http://www.ia15.org")
html = response.read()
print(html)
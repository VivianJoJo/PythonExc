__author__ = 'vivian'

# coding:utf8

from urllib import request
import http.cookiejar

url = "http://www.baidu.com"

print('way 1')
response1 = request.urlopen(url)
print(response1.getcode())
print(len(response1.read()))

print('way 2')
req = request.Request(url)
req.add_header("user-agent", "Mozilla/5.0")
response2 = request.urlopen(req)
print(response2.getcode())
print(len(response2.read()))

print('way 3')
cj = http.cookiejar.CookieJar()
opener = request.build_opener(request.HTTPCookieProcessor(cj))
request.install_opener(opener)
response3 = request.urlopen(url)
print(response3.getcode())
print(cj)
print(response3.read())
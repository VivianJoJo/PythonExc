import re

__author__ = 'vivian'


from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

# print bs4
# a
soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')
print('find all href')
links = soup.find_all('a')
for link in links:
    print(link.name, link['href'], link.get_text())

#
print('lacie')
link_node = soup.find('a', href='http://example.com/lacie')
print(link_node.name, link_node['href'], link_node.get_text())

#
print('zheng ze pi pei')
link_node = soup.find('a', href=re.compile(r"ill"))
print(link_node.name, link_node['href'], link_node.get_text())

#
print('title text')
title_node = soup.find('title')
print(title_node.name, title_node.get_text())

#
print('p text')
# p_node = soup.find('p', class_='story')
p_node = soup.find('p', {"class": "title"})

print(p_node.name, p_node.get_text())

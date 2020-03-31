import requests
from urllib.parse import quote_plus
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver

# base_url = 'https://www.google.com/search?q='

# search_url = quote_plus(input('검색어 입력 : '))

# url = 

# driver = webdriver.Chrome()
# driver.get(url)

# html = driver.page_source

# soup = BeautifulSoup(html, 'html.parser')

# results = soup.find_all(class_ = 'r')

# data = {}

# for i in results:
#     try:
#         data[i.text] = i.get('href')

#     except AttributeError:
#         print('None')

# driver.close()
search = input("검색어 입력 : ")
url = f'https://search.naver.com/search.naver?where=post&sm=tab_jum&query={quote_plus(search)}'
        
html = urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

results = soup.find_all(class_ = 'sh_blog_title')

for result in results:
    print(result.attrs['title'])
    print(result.attrs['href'])
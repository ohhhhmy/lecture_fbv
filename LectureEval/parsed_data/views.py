from django.shortcuts import render
from django.views import views
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
from urllib.request import urlopen


# def parse_data():
#     if request.method == "POST":
#         search = request.POST['search']
#         url = f'https://search.naver.com/search.naver?where=post&sm=tab_jum&query={quote_plus(search)}'
        
#         html = urlopen(url).read()
#         soup = BeautifulSoup(html, 'html.parser')
#         html.close()
        
#         results = soup.find_all('a')
        
#         data = {}
#         for i in results:
#             data[i.attrs['title']] = i.attrs['href']
#             return data

#     else:
#         return render(request, 'search.html')









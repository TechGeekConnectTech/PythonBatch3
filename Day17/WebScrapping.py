from bs4 import BeautifulSoup
import requests

url='https://www.bbc.com/news'
response=requests.get(url)
soup=BeautifulSoup(response.text,'html.parser')
print(soup.title.string)
# print all headings in the page

headings=soup.find_all(['h1','h2','h3','h4','h5','h6'])
news_bbc=[]
for heading in headings:
    news_bbc.append(heading.string)


url='https://www.nseindia.com/'
response=requests.get(url)
soup=BeautifulSoup(response.text,'html.parser')
print(soup.title.string)
# print all headings in the page
toi=[]
headings=soup.find_all('h2')   
for heading in headings:
    toi.append(heading.string)
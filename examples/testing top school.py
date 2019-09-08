import requests
import pandas
from bs4 import BeautifulSoup
s=requests.get('http://www.mastersindatascience.org/schools/23-great-schools-with-masters-programs-in-data-science/')
soup=BeautifulSoup(s.text,"html.parser")
'''for entry in soup.select('.top-featured.cat-1'):
        print(entry.select('h3')[0].text)       
        print(entry.select('h4')[0].text)            
        print(entry.select('ul')[0].text)
        print()'''
for entry in soup.select('.featured-listing.usfc-listing'):
        print(entry.select('h3')[0].text)                  
        print(entry.select('ul')[0].text)
        print()
for entry in soup.select('li'):
    if entry.select('br'):
        continue
    elif entry.select('h4'):
        print(entry.select('h3')[0].text,entry.select('h4')[0].text,entry.select('ul')[0].text)
        print()
       

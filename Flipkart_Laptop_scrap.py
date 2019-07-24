from bs4 import BeautifulSoup
import re
import csv
import pandas as pd
import requests

url = "https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniq"
response = requests.get(url)
#print(response)
data = response.text
#print(data)
soup =BeautifulSoup(data, 'html.parser')
#print(soup)
#tags = soup.find_all('a')
#print(tags)
products = []
price = []
ratings = []
for a in soup.findAll('a',attrs={'class':'_31qSD5'}):
   name = a.find('div',attrs={'class':'_3wU53n'})
   prices = a.find('div',attrs={'class':'_6BWGkk'})
   rate = a.find('div',attrs={'class':'hGSR34'})
   print(name.text)
   print(prices.text)
   print(rate.text)
   products.append(name.text)
   price.append(prices.text)
   ratings.append(rate.text)
print(products)
print(price)
print(ratings)
df = pd.DataFrame({'Product Name':products, 'Price': price, 'Rating':ratings}) 
df.to_csv('Flipkart.csv', index=False, encoding='utf-8')	




	   
	
   
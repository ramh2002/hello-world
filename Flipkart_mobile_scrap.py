from bs4 import BeautifulSoup
import re
import csv
import pandas as pd
import requests

url = "https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.serviceability%5B%5D%3Dfalse&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_r"
response = requests.get(url)
data = response.text
soup =BeautifulSoup(data, 'html.parser')
products = []
price = []
ratings = []
Actual_Rate = []
Discuounts = []
for a in soup.findAll('a',attrs={'class':'_31qSD5'}):
   name = a.find('div',attrs={'class':'_3wU53n'})
   prices = a.find('div',attrs={'class':'_1vC4OE _2rQ-NK'})
   rate = a.find('div',attrs={'class':'hGSR34'})
   Actual_price = a.find('div',attrs={'class':'_3auQ3N _2GcJzG'})
   Discount = a.find('div',attrs={'class':'VGWI6T'})
   products.append(name.text)
   price.append(prices.text)
   ratings.append(rate.text)
   Actual_Rate.append(Actual_price.text)
   Discuounts.append(Discount.text)
df = pd.DataFrame({'Product Name':products, 'Price': price, 'Actual_Price':Actual_Rate, 'Discount': Discuounts, 'Rating':ratings}) 
df.to_csv('Flipkart_mobile_offers.csv', index=False, encoding='utf-8')	




	   
	
   
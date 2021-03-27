import requests
from bs4 import BeautifulSoup

url = 'https://covid.cdc.gov/covid-data-tracker/'
the_word = 'Vaccinations'
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
html = response.content

soup = BeautifulSoup(html)
words = soup.find(text=lambda text: text and the_word in text)
print(words)
count =  len(words)
print('\nUrl: {}\ncontains {} occurrences of word: {}'.format(url, count, the_word))

##print (soup.prettify())

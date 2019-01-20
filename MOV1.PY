from bs4 import BeautifulSoup
import urllib.parse
import requests
from selenium import webdriver
from urllib.request import urlopen as uReq




search_item = 'showtimes for october in delhi'  ## search query
url = "https://www.google.co.in/search?q=" + search_item

uClient = uReq(url)
p_html  = uClient.read()
uClient.close()
p_soup = BeautifulSoup(p_html, 'html.parser')

maa= p_soup.find('a')




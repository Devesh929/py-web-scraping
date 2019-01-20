
from bs4 import BeautifulSoup
import requests

res = requests.get('https://paytm.com/movies/delhi/october-m/O9IX6F?fromdate=2018-05-06')
soup = BeautifulSoup(res.text, 'lxml')

#news_box = soup.find('div', {'class': '_2tt5'})
#all_news = news_box.find_all('a')
#print (all_news)

#for news in all_news:

    #print(news.text)
  #  print()


#for item in soup.select("._2jBq"):
c=soup.select('li._2tt5._2gza')
          #print (item.text)
print (c[0].text)
#a=c[0].text
#sep="C"
#rest = a.split(sep, 1)[0]
#print(rest)
        



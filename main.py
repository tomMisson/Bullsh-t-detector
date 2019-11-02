#comment

import requests
import urllib.request
import time
from bs4 import BeautifulSoup

print("Here")

url = 'https://www.bbc.co.uk/news/uk-england-50273590'
response = requests.get(url)
'''
print(response)

soup = BeautifulSoup(response.text, "html.parser")

for i in range (36,len(soup.findAll('p'))+1):
	one_a_tag = soup.findAll('p')[36]
	link = one_a_tag['href']

	download_url = 'https://www.bbc.co.uk/news/' + link
	urllib.request.urlretrieve(download_url,'./' +link[link.find('/turnstile_')+1:]) 

	time.sleep(1)
'''

response = requests.get(url)
coverpage = response.content

soup1 = BeautifulSoup(coverpage, 'html5llib')

coverpage_news = soup1.find_all('p', class_='media-landscape has-caption full-width')

coverpage_news[4].get_text()

coverpage_news[4]['href']

'''time.sleep(1)'''

# Scraping the first 5 articles
number_of_articles = 5
# Empty lists for content, links and titles
news_contents = []
list_links = []
list_titles = []

for n in np.arange(0, number_of_articles):
    '''
	# only news articles (there are also albums and other things)
    if "inenglish" not in coverpage_news[n].find('p')['href']:  
        continue
    '''
    # Getting the link of the article
    link = coverpage_news[n].find('p')['href']
    list_links.append(link)
    
    # Getting the title
    title = coverpage_news[n].find('p').get_text()
    list_titles.append(title)
    
    # Reading the content (it is divided in paragraphs)
    article = requests.get(link)
    article_content = article.content
    soup_article = BeautifulSoup(article_content, 'html5lib')
    body = soup_article.find_all('div', class_='media-landscape has-caption full-width')
    x = body[0].find_all('p')
    
    # Unifying the paragraphs
    list_paragraphs = []
    for p in np.arange(0, len(x)):
        paragraph = x[p].get_text()
        list_paragraphs.append(paragraph)
        final_article = " ".join(list_paragraphs)
        
    news_contents.append(final_article)
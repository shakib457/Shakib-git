import requests
from bs4 import BeautifulSoup

url = 'https://www.w3schools.com/python/default.asp'
response = requests.get(url)
if response.status_code == 200:
    html_text = response.text

    soup = BeautifulSoup(html_text, 'html.parser')
    items = soup.find_all('ul', attrs = {'class': 'checklist'})
    print(len(items))
    titles = items[0].find_all('a')
    print(titles)

    if len(titles) > 0:
        for title in titles:
            print(title.getText())

    else:
        print('we coud not find any title')

    print(soup)
    tag_a = soup.find_all('a')
    
    for link in tag_a:
        
        print(link.get('href'))
    print(html_text)
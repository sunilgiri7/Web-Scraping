''' Beautiful Soup can be used to extract data from HTML documents, 
and then lxml/parser can be used to process and manipulate that data. 
This combination allows developers to easily and efficiently extract and process data from web pages, 
which is useful for a variety of applications such as data mining, web scraping, and automated testing.'''

from bs4 import BeautifulSoup
with open('index.html', 'r',encoding='utf-8') as html_content:
    content = html_content.read()
    # print(content)

    soup = BeautifulSoup(content, 'html.parser')
    tags = soup.find_all('h2')
    print(tags)
    for words in tags:
        print(words.text)

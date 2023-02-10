# A News API for news retrieval
import requests
import json

# prompt for entering a user's news API key
API_key = input('Please enter your News API Key: ')

topic = input('Please enter the news topic that you want: ')
num = input('Please enter the number (not exceeding 100) of news you want: ')
date = input('Please enter the start date in the form like \'2022-02-01\', then you will get news from this day: ')

url = ('http://newsapi.org/v2/everything?'
       'q='+topic+'&'
       'from='+date+'&'
       'sortBy=popularity&'
       'pageSize='+num+'&'
       'apiKey='+API_key)

response = requests.get(url)
output = json.dumps(response.json(), indent=4)
f = open('News.txt', 'w', encoding='utf-8')
for i in output:
    f.write(i)

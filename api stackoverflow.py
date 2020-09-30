import requests
import datetime

today = datetime.datetime.today()
day_before_yest = today - datetime.timedelta(days=2)

unix_today = int(today.timestamp())
unix_day_before_yest = int(day_before_yest.timestamp())

param = {'fromdate': unix_day_before_yest, 'todate': unix_today}

response = requests.get('https://api.stackexchange.com/2.2/questions?\
&sort=creation&tagged=python&site=stackoverflow', params=param)

items_list = response.json()['items']

print('Новости за последние два дня по тегу Python:')
for news_tag_python in items_list:
	print(news_tag_python['link'])

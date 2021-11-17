import requests
import json

url = 'https://movie.douban.com/j/chart/top_list'
param ={
    'type':'24',
    'interval_id':'100:90',
    'action':'',
    'start':'40',
    'limit':'20',
}
headers = {
       'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    } # 谷歌浏览器身份标识
response = requests.get(url= url , params=param , headers=headers)

list_data = response.json()

fp = open('./douban.json', 'w' , encoding='utf-8')
json.dump(list_data , fp= fp , ensure_ascii=False)
print("over!")
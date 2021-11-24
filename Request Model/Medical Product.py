import json
import requests
import random
from time import sleep

if __name__ == "__main__":

    id_list = []

    def get_id(page):
        sleep(random.uniform(0,1))  # 随机出现1，2之间的数字包括小数使程序休息，不让访问进行的那么快
        headers = {
                'Connection': 'keep-alive',
                'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'
        }
        url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
        params = {
            'on':' true',
            'page': page,
            'pageSize':'15',
            'productName':'',
            'conditionType':'1',
            'applyname':'',
            'applysn':''
        }
        json_ids = requests.post(url= url, headers=headers, data=params).json()
        for dic in json_ids['list']:
            id_list.append(dic['ID'])
        return id_list

    def get_index(id):
        detail_list = []
        sleep(random.uniform(0, 1))  # 随机出现1，2之间的数字包括小数使程序休息，不让访问进行的那么快
        headers = {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'
        }
        url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
        data = {
            'id': id
        }
        detail = requests.post(url=url , headers=headers,data=data).json()
        detail_list.append(detail)
        return detail_list


    for page in range(1,2):
        page_id = get_id(page)
        print("第" + str(page) + "页提取完成")
        print(page_id)
    fp = open('Medical Product Detail.json', 'a', encoding='utf-8')
    for id in page_id:
        page_de = get_index(id)
        json.dump(page_de,fp=fp,ensure_ascii=False)
    print('over')




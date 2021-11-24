import requests
import random
from time import sleep

if __name__ == "__main__":

    def get_page(page):
        n = 3
        try:
            sleep(random.uniform(1, 2))#随机出现1，2之间的数字包括小数使程序休息，不让访问进行的那么快
            headers = {
                'Connection': 'keep-alive',
                'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'
            }
            data = {
                'cname': '',
                'pid': '',
                'keyword': '上海',
                'pageIndex': page,
                'pageSize': '10'
            }
            url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
            try:
                response = requests.post(url=url, data=data, headers=headers)
                print(response.status_code)
                text = response.text
                print(text)
                return text #返回取得的json
            except requests.ConnectionError as e:
                print('error', e.args)
        except(TimeoutError, Exception):
            n -= 1
            if n == 0:
                print('请求三次均失败，放弃此请求，检查请求条件')
                return
            else:
                print('请求失败。重新请求')


with open('KFC.json', 'a' , encoding='utf-8') as fp:#变量为a时，可多次写入，w时会覆盖
    for page in range(1,7):
        pages = get_page(page)
        fp.write(pages+"\n")
        print("第" + str(page) + "页提取完成")
print("提取结束")


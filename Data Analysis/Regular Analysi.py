import re
import os
import requests

if __name__ == "__main__":
    if not os.path.exists('./graphdata'):
        os.mkdir('./graphdata')
    headers = {
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'
    }
    url = 'https://www.qiushibaike.com/imgrank/'
    ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
    page_text = requests.get(url=url, headers= headers).text
    img_src_list = re.findall(ex,page_text,re.S)
    #print(img_src_list)
    for src in img_src_list:
        src = 'http:' + src
        img_data = requests.get(url=src , headers=headers).content
        img_name = src.split('/')[-1]
        img_path = './graphdata/' + img_name
        with open(img_path ,'wb' ) as fp :
            fp.write(img_data)
            print(img_name+'download success')

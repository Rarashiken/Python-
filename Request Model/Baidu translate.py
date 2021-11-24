import json

import requests
'''
页面局部刷新：ajax
#Response Headers：客户端响应的请求
    Content-type:响应请求的种类
#过程：
    - post请求（带参数）
    - 响应数据是一组json数据
    - text/html; charset=shift_jis
        它的意思是设置页面内容是html。
        Shift_JIS主要是Windows和Macintosh使用的文字编码。（日文）
        
'''
if __name__ == "__main__":
    #step1: 指定url
    post_url = 'https://fanyi.baidu.com/sug'
    #step2.UA伪装：将对应的UA封装到一个字典中
    headers = {
       'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    } # 谷歌浏览器身份标识

    #step3.post请求参数处理
    data = {
        'kw' : 'dog'
    }
    #step4.请求发送
    response = requests.post(url=post_url ,data = data ,headers= headers )
    #step5.获取相应数据:json（）方法返回obj（如果确认服务器响应数据是json类型才可使用json()）
    dic_obj = response.json()
    print(dic_obj)
    #持久化存储
    fp = open('dog.json', 'w', encoding='utf-8')
    json.dump(dic_obj,fp=fp , ensure_ascii=False)

    print('Over')
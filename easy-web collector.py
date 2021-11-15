import requests
'''
#UA：User-Agent（请求载体的身份标识）
#反爬机制；UA检测----门户网站的服务器会检测对应请求的载体身份标识，如果检测到请求的载体身份标识为某一款浏览器
说明该请求是一个正常请求。但是，如果检测到请求的载体身份标识不是基于某一款浏览器的，则表示该请求为不正常的请求（爬虫）
为不正常的请求的情况下，则服务器端会有可能拒绝该次请求

#UA伪装：让爬虫对应的请求载体身份标识伪装成某一款浏览器
'''


if __name__ == "__main__":
    # UA伪装：将对应的UA封装到一个字典中
    headers = {
       'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    } # 谷歌浏览器身份标识
    url = 'https://www.sogou.com/web'
    #处理URL携带的参数：封装到字典中
    kw = input('enter a word:')
    param ={
        'query': kw
    }
    #对指定URL发起的请求对应的URL是携带参数的，且请求过程中处理了参数
    response = requests.get(url=url , params=param , headers=headers)
    page_text = response.text

    fileName = kw+'.html'
    with open(fileName , 'w' , encoding='utf-8') as fp:
        fp.write(page_text)
    print(fileName,'Save Succece')
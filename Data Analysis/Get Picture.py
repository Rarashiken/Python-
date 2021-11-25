import requests

if __name__ == "__main__":
    headers = {
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'
    }
    url = 'https://pic.qiushibaike.com/system/pictures/12481/124818016/medium/AH0AI6I8ROD4L46B.jpg'
    # content返回二进制形式图片数据
    # text（字符串） content（二进制） json()（对象类型响应数据）
    re = requests.get(url= url, headers=headers).content
    # b指二进制文件，wb指打开一个只写的二进制文件
    with open('./Qiutu.jpg','wb') as fp:
        fp.write(re)

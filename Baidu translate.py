import requests
'''
页面局部刷新：ajax
#Response Headers：客户端响应的请求
    Content-type:响应请求的种类
#过程：
    - post请求（带参数）
    - 响应数据是一组json数据
    - Shift_JIS主要是Windows和Macintosh使用的文字编码。（日文）
'''
if __name__ == "__main__":
    # UA伪装：将对应的UA封装到一个字典中
    headers = {
       'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    } # 谷歌浏览器身份标识

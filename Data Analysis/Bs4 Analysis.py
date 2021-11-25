from bs4 import BeautifulSoup

if __name__ == "__main__":
    headers = {
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'
    }
    fp = open('./test.html' , 'r' , encoding='utf-8')
    soup = BeautifulSoup(fp,'lxml')
    #print(soup.a) #soup.tagName 返回的是html中国呢第一次出现的tagName标签
    #print(soup.find('div'))
    #print(soup.find('div', class_= 'hzbscbox').string)
    #print(soup.find_all('div'))
    #print(soup.select('.dzpzmain'))
    #print(soup.select('.hzbscbox >div span   ')[0])
    #print(soup.select('.hzbscbox >div span   ')[0].get_text())
    print(soup.select('.hzbscin > div span')[0]['id'])


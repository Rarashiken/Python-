from bs4 import BeautifulSoup
import requests
#练习了爬取在线读小说网站的内容
if __name__ == "__main__":
    headers = {
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'
    }
    url = 'https://sanguo.5000yan.com/'
    page_text = requests.get(url=url,headers=headers)
    #解决乱码 或者 res.encoding = "page_text.apparent_encoding"返回的内容 一般中文为utf-8
    page_text.encoding = page_text.apparent_encoding
    #print(page_text.text)


    soup = BeautifulSoup(page_text.text,'lxml')
    li_list = soup.select('main > div > ul > li')
    print(li_list)
    fp = open('./sanguo.txt','w',encoding='utf-8')
    for li in li_list:
        title = li.a.string
        detail_url = li.a['href']
        detaul_page_text = requests.get(url=detail_url ,headers=headers)
        detaul_page_text.encoding = "utf-8"
        detail_soup = BeautifulSoup(detaul_page_text.text,'lxml')
        div_tag = detail_soup.find('div',class_= 'grap')
        content = div_tag.text
        fp.write(title +":" + content + "\n")
        print(title ,"爬取成功")
        #爬取到的数据中有很多nbsp，在html里 &nbsp就是代表空格





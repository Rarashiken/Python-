import re

key = "javapythonc++php"
p = re.findall('python',key)[0]
print(p)

key = "<html><h1>hello world<h1><html>"
p = re.findall('<h1>(.*)<h1>',key)[0]
print(p)

string = '我喜欢的女孩身高158'
p = re.findall('\d+', string)
print(p)

key = 'http://www.baidu.com/ and https://www.google.com/ and '
p = re.findall('http?s://',key)
print(p)

key = 'lalala<hTml>hello</HtMl>hahah'
p = re.findall('<[Hh][Tt][Mm][Ll]>(.*)</[Hh][Tt][Mm][Ll]>', key)
print(p)

key = 'bobo@hit.edu.com'
p = re.findall('h.*?\.', key)
print(p)

key = 'saas and sas and saaas'
p = re.findall('sa{1,2}s',key)
print(p)


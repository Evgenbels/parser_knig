import requests as rq
from bs4 import BeautifulSoup as bfs

url="https://akniga.xyz/popadancy/page/2/"
r=rq.get(url)

soup=bfs(r.text,'html.parser')
npp=1
items=soup.find_all('div',class_='short-item')
knigi=[]
for item in items:
    # soupit=bfs(item,'html.parser')
    ul=item.find('ul',class_='short-list')
    print(ul)
    lis=ul.find_all('li')
    if lis.len()<4 :
        next(items)
    li=lis[4]
    a=li.find('a')
    h=li.find('a').get('href')
    knigi.append(
        {
            'npp':npp,
            'title':item.find('a',class_='short-title').get_text(),
             'god':lis[0].get_text(),
             'avtor':lis[1].get_text(),
             'akter':lis[2].get_text(),
             'time':lis[3].get_text(),
             'sikl':lis[4].get_text(),
             'sikl_href':a.get('href'),
             'ws1':li.contents[-1]
        }
    )
    # print (npp)
    # print()
    # # print (item)
    # print (li)
    npp+=1
for ws in knigi:
    print(ws)

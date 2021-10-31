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
    knigi.append(
        {
            'npp':npp,
            'title':item.find('a',class_='short-title').get_text(),
            'god':item.find('li').get_text(),
            'avtor':item.next_element.get_text()
        }
    )
    # print (npp)
    # print(ws)
    # print()
    # print (item)
    npp+=1
print(knigi)

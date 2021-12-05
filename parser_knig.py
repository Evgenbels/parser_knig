import requests as rq
from bs4 import BeautifulSoup as bfs
import pymysql
from getpass import getpass

def ppr_kol(siklHref):
    # url=knigi[0]['sikl_href']
    # r=rq.get(url)
    # soup=bfs(r.text,'html.parser')
    # items=soup.find_all('div',class_='short-item')
    return len(bfs(rq.get(siklHref).text,'html.parser').find_all('div',class_='short-item'))


url="https://akniga.xyz/popadancy/page/2/"
r=rq.get(url)

soup=bfs(r.text,'html.parser')
npp=1
items=soup.find_all('div',class_='short-item')
knigi=[]
#    Подключение MySQL
con = pymysql.connect(host='localhost',
    user='root',
    password=getpass("Пароль: "),
    db='parser_knig',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor)
# try:
#     with con as connection:
#         print(connection)
cur = con.cursor()



for item in items:
    # soupit=bfs(item,'html.parser')
    ul=item.find('ul',class_='short-list')
    # print(ul)
    lis=ul.find_all('li')
    # print('/n/n',len(lis))
    if len(lis)<=4 :
        # next(items)
        print("\nNext\n",item.find('a',class_='short-title').get_text(),"\n\n")
        continue
    li1=lis[1]
    a1=li1.find('a')
    avtor=a1.get_text()

    li=lis[4]
    a=li.find('a')
    sikl=a.get_text()
    
    sikl_count=ppr_kol(a.get('href'))
    
    h=li.find('a').get('href')
    # print(lis[1].get_text())
    wsSql="SELECT * FROM knigi WHERE avtor='"+avtor+"' and cikl='"+sikl+"'"
    print(wsSql)
    cur.execute(wsSql)
    # cur.execute("SELECT * FROM knigi") SELECT * FROM knigi where avtor='belyev' and cikl='home'
    # cur.execute("SELECT * FROM knigi WHERE avtor='%s' and cikl='%s'", lis[1].get_text(),lis[4].get_text())
    # cur.execute("SELECT * FROM knigi WHERE avtor='belyev' and cikl='home11'")
    if cur.rowcount<1 :
        wsSqlIns="INSERT INTO knigi (avtor,cikl,kol,flag) VALUES ('"+avtor+"','"+sikl+"',"+str(sikl_count)+",0)"
        cur.execute(wsSqlIns)
        # cur.commit()
    # rows  = cur.fetchall()
    # for row in rows:
    #     print(row['avtor'],row['cikl'])
    knigi.append(
        {
            'npp':npp,
            'title':item.find('a',class_='short-title').get_text(),
             'god':lis[0].get_text(),
             'avtor':avtor,
             'akter':lis[2].get_text(),
             'time':lis[3].get_text(),
             'sikl':sikl,
             'sikl_href':a.get('href'),
             'sikl_npp':li.contents[-1],
             'sikl_count':sikl_count
        }
    )
    # print (npp)
    # print()
    # # print (item)
    # print (li)
    npp+=1
# for ws in knigi:
#     print(ws)
for ws in knigi:
    print(ws['npp'],ws['avtor'],ws['sikl'],ws['sikl_npp'],ws['sikl_count'])

print(len(knigi))
print(knigi[0]['npp'])
url=knigi[0]['sikl_href']
r=rq.get(url)
soup=bfs(r.text,'html.parser')
items=soup.find_all('div',class_='short-item')
print(len(items))

cur.close()
con.commit()
import requests as rq
from bs4 import BeautifulSoup as bfs

html_doc = """
<div class="short-item">
	<div class="short-cols fx-row">
		<a class="short-img img-fit" href="https://akniga.xyz/26540-knjaz-mescherskij-drozdov-anatolij.html">
			<img src="/uploads/posts/2021-10/616658fda5dfe.jpg" alt="Князь Мещерский - Дроздов Анатолий">
		</a>
		<div class="short-desc fx-1 fx-col fx-between">           
			<div class="short-header fx-row fx-middle">
				<a class="short-title fx-1" href="https://akniga.xyz/26540-knjaz-mescherskij-drozdov-anatolij.html">Князь Мещерский - Дроздов Анатолий</a>
                
			</div>
			<ul class="short-list">
				<li><span>Год начитки:</span> 2020</li>
                <li><span>Автор:</span> <a href="https://akniga.xyz/xfsearch/avtor/%D0%94%D1%80%D0%BE%D0%B7%D0%B4%D0%BE%D0%B2%20%D0%90%D0%BD%D0%B0%D1%82%D0%BE%D0%BB%D0%B8%D0%B9/">Дроздов Анатолий</a></li>
				<li><span>Читает:</span> <a href="https://akniga.xyz/xfsearch/chitaet/%D0%9F%D1%83%D0%B3%D0%B0%D1%87%D0%B5%D0%B2%20%D0%92%D0%B0%D0%B4%D0%B8%D0%BC/">Пугачев Вадим</a></li>
                <li><span>Время:</span> 9:59:43</li>
                <li><span>Цикл:</span> <a href="https://akniga.xyz/xfsearch/cikl/%D0%97%D0%B0%D1%83%D1%80%D1%8F%D0%B4-%D0%B2%D1%80%D0%B0%D1%87/">Зауряд-врач</a> №3 </li> 
			</ul>
			<div class="short-meta fx-row fx-middle icon-left">	
				<div class="mrating">
                    <div id="ratig-layer-26540">
	                    <div class="rating">
                            <ul class="unit-rating">
                            <li class="current-rating" style="width:80%;">80</li>
                            <li><a href="#" title="Плохо" class="r1-unit" onclick="doRate('1', '26540'); return false;">1</a></li>
                            <li><a href="#" title="Приемлемо" class="r2-unit" onclick="doRate('2', '26540'); return false;">2</a></li>
                            <li><a href="#" title="Средне" class="r3-unit" onclick="doRate('3', '26540'); return false;">3</a></li>
                            <li><a href="#" title="Хорошо" class="r4-unit" onclick="doRate('4', '26540'); return false;">4</a></li>
                            <li><a href="#" title="Отлично" class="r5-unit" onclick="doRate('5', '26540'); return false;">5</a></li>
                            </ul>
                    	</div>
                    </div>
                </div>
				
				<div class="short-meta-item"><span class="fal fa-calendar-alt"></span>13.10.2021</div>
				
                <a href="https://akniga.xyz/26540-knjaz-mescherskij-drozdov-anatolij.html" class="short-btn btn">Скачать</a>
			</div>
		</div>
	</div>
</div>
"""
url="https://akniga.xyz/popadancy/page/2/"
r=rq.get(url)

soup=bfs(r.text,'html.parser')
# soup = bfs (html_doc, 'html.parser')

#print(soup.prettify())
items=soup.find_all('div',class_='short-item')
for item in items:
    ul=item.find('ul',class_='short-list')
    # print(ul)
    lis=ul.find_all('li')
    # for li in lis:
    #     print(li)
    #     print(li.get_text())
    li=lis[4]
    print(li)
    print(li.text)
    a=li.find('a')
    print(a.text)
    
    print(a.get('href'))
    print(li.contents[-1].text)
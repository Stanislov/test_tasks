# Извлечение мероприятий с сайта www.python.org/

from urllib.request import urlopen
from bs4 import BeautifulSoup


url = 'https://www.python.org/'
html = urlopen(url)
soup = BeautifulSoup(html.read(), "lxml")

upp_e = soup.find('div', attrs={'class':'medium-widget event-widget last'})
upp_e2 = upp_e.find('ul', attrs={'class':'menu'})
p2020 = [x for x in upp_e2.findAll('li')]

# m1 - текущий месяц, m2 - следующий месяц
mondays, monday1, monday2, m1, m2 = [], [], [], 12, 1
for i in p2020:
	a = ['','','']
	a[0] = i.time.text
	a[1] = i.a.text
	a[2] = url[:-1]+i.a['href']
	mondays.append(a)
	
print()
print()
for m in mondays:
	if int(m[0][5:7])==m1:
		monday1.append(m[0]+' '+m[1]+' '+m[2])
	elif int(m[0][5:7])==m2:
		monday2.append(m[0]+' '+m[1]+' '+m[2])

print('---------------------------------------')
print('Мероприятия текущего месяца')
for n1 in monday1: 
	print(n1)
print()
print('Мероприятия следующего месяца')
for n2 in monday2: 
	print(n2)
print('---------------------------------------')

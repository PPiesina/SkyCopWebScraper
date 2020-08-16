import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

import urllib.parse
import requests




#Loging in and creating session
payload = {  "username": 'SkycopSkycop',  "password": 'gqyzpg3MeM6hA8C' }

s = requests.session()

log_in_web = s.post('https://www.ch-aviation.com/login?od=http%3A%2F%2Fwww.ch-aviation.com%2Fportal%2Fairlines%2Fsearch%3Fsearch%3D1%26geo%3Dbase%26page%3D0', payload)



#I will put for loop here when script is done

my_url = 'https://www.ch-aviation.com/portal/airlines/search?search=1&geo=base&page=0'

r2 = s.get(my_url)



page_soup = soup(r2.text, "html.parser")

t_rows = page_soup.findAll("tr")



links = []

for i in range(len(t_rows)):
	if i == 0:
		i += 1
	rw = t_rows[i]
	link_grab = rw.a["href"]
	links.append(link_grab)



r3 = s.get(links[0])


info_soup = soup(r3.text, "html.parser")

print(info_soup)








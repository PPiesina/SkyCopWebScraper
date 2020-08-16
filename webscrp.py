import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


import mechanize
import http.cookiejar as cookielib


import urllib.parse
import requests

'''
cj = cookielib.CookieJar()
br = mechanize.Browser()
br.set_cookiejar(cj)
br.open("https://www.ch-aviation.com/login?od=http%3A%2F%2Fwww.ch-aviation.com%2Fportal%2Fairline%2FXA1")
br.select_form(nr=0)
br.form['username'] = 'SkycopSkycop'
br.form['password'] = 'gqyzpg3MeM6hA8C'
br.submit()
'''

#print(br.response().read())


my_url = 'https://www.ch-aviation.com/portal/airlines/search?search=1&geo=base&page=0'

# Taking The Page
uClient = uReq(my_url)

page_html = uClient.read()

uClient.close()


#parsing to html
page_soup = soup(page_html, "html.parser")
#print(page_soup)
#Getting table rows
t_rows = page_soup.findAll("tr")



rw = t_rows[2]

link_grab = rw.a["href"]

print(link_grab)

	#https://www.ch-aviation.com/login?od=http%3A%2F%2Fwww.ch-aviation.com%2Fportal%2Fairline%2FQ5



cj = cookielib.CookieJar()
br = mechanize.Browser()
br.set_cookiejar(cj)
sess = requests.Session()
br.open("https://www.ch-aviation.com/login?od=http%3A%2F%2Fwww.ch-aviation.com%2Fportal%2Fairline%2FXA1")
br.select_form(nr=0)
br.form['username'] = 'SkycopSkycop'
br.form['password'] = 'gqyzpg3MeM6hA8C'
br.submit()

temp_page_html = br.response().read()
temp_page_soup = soup(temp_page_html, "html.parser")
br.response().close()


my_urlAA = 'https://www.ch-aviation.com/portal/airlines/search?search=1&geo=base&page=1'

# Taking The Page
username = "SkycopSkycop"
password = "gqyzpg3MeM6hA8C"
sauce = requests.get(my_urlAA, auth=(username, password))
sauce = sauce.content
soups = soup(sauce,"html.parser")
print(soups)

#print(temp_page_soup)
#print(nothing)


#print(temp_page_soup)
	



	#t_divs = temp_page_soup.findAll("div",{"class","account-box"})
	#print(t_divs[0])



'''
	for x in range(len(t_divs)):

		divWithInfo = t_divs[x].find("div","info")

		print(divWithInfo)
'''

	
'''

<div class="account-box">    <a href="https://www.ch-aviation.com/login?od=http%3A%2F%2Fwww.ch-aviation.com%2Fportal%2Fairline%2FXA1">
        Login
    </a>
    <a href="http://blog.ch-aviation.com">
        Blog
    </a>
    <a href="https://www.ch-aviation.com/portal/about">
        About us
    </a>
    <a href="https://www.ch-aviation.com/portal/subscribe" class="first">
        Pricing and Sign-Up
    </a>
</div>

'''
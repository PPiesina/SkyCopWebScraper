import requests
from lxml import html

import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

USERNAME = "SkycopSkycop"
PASSWORD = "gqyzpg3MeM6hA8C"

LOGIN_URL = "https://www.ch-aviation.com/login?od=http%3A%2F%2Fwww.ch-aviation.com%2Fportal%2Findex"
URL = "https://www.ch-aviation.com/portal/airline/XA1"

def main():
    session_requests = requests.session()

    # Get login csrf token
    result = session_requests.get(LOGIN_URL)
    tree = html.fromstring(result.text)
    authenticity_token = list(set(tree.xpath("//input[@name='originalDestination']/@value")))[0]


    # Create payload
    payload = {
        "username": USERNAME, 
        "password": PASSWORD, 
        "csrfmiddlewaretoken": authenticity_token #originalDestination
    }

    # Perform login
    result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))

    # Scrape url




    
    result = session_requests.get(URL, headers = dict(referer = URL))


    print(result)
    tree = html.fromstring(result.content)
    print(tree)
    bucket_names = tree.xpath("//div[@class='repo-list--repo']/a/text()")

    print(bucket_names)
    

if __name__ == '__main__':
    main()
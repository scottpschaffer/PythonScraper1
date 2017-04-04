from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests

with requests.Session() as session:
    page_number = 1
    #url = 'https://apps.health.tn.gov/EHInspections/'
    url = 'https://apps.health.tn.gov/EHInspections/EHInspections/GetSearchResults?ProgramID=0605&SearchTerms=Burger+King&_search=false'
    #&nd=1490901099494&rows=auto&page=1&sidx=&sord=asc'

    while True:
        print("Processing page: #{page_number}; url: {url}".format(page_number=page_number, url=url))
        response = session.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        print(soup)
        x1 = soup.findAll('select')
        #print(x1[0])
        x2 = soup.findAll('input')
        for x in x2:
            print(x)
        # check if there is next page, break if not
        next_link = soup.find("a", text="next")
        if next_link is None:
            break

        url = urljoin(url, next_link["href"])
        page_number += 1
    
    print("Done")
    print("aaa")
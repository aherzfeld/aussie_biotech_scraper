import requests
from bs4 import BeautifulSoup

# Web scraper to extract exhibitor info from Aussie Biotech website

url = 'http://ausbiotechnc.org/exhibition/exhibiting-companies'

r = requests.get(url)

# make sure page exists
if r.status_code == 200:
    html = r.text

soup = BeautifulSoup(html, 'html.parser')

# print(soup.prettify())  # for testing

tbody = soup.tbody

results = []
for tr in tbody.children:
    print(tr, type(tr))
    """if tr.a:
        data = {'name': '', 'url': '', 'loc': ''}
        data['url'] = (tr.contents)[0].a['href']
        data['name'] = (tr.contents)[1].h1.contents
        data['loc'] = (tr.contents)[1].p.contents
        results.append(data)"""

print(results)

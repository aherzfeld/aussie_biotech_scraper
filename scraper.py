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

rows = tbody.find_all('tr')

for row in rows:
    if row.a:
        data = {'name': '', 'url': '', 'loc': ''}
        tds = row.find_all('td')
        data['url'] = tds[0].a['href']
        data['name'] = str(tds[1].h3.contents[0])
        data['loc'] = str(tds[1].p.contents[0])
        results.append(data)
print(results)

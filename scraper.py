import csv
import requests
from bs4 import BeautifulSoup

# Web scraper to extract exhibitor info from Aussie Biotech website

url = 'http://ausbiotechnc.org/exhibition/exhibiting-companies'

r = requests.get(url)

# make sure page exists
if r.status_code == 200:
    html = r.text

# Extract data using BeautifulSoup

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

# Save data to csv file

with open('aussie_biotech.csv', mode='w') as csv_file:
    fieldnames = ['name', 'url', 'loc']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for row in results:
        writer.writerow(row)

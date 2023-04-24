import requests
from bs4 import BeautifulSoup

url = 'https://www.prisonstudies.org/world-prison-brief-data'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table', {'id': 'table_2'})
rows = table.find_all('tr')

for row in rows:
    cells = row.find_all('td')
    if len(cells) == 5:
        country = cells[0].text.strip()
        prison_population = int(cells[1].text.replace(',', ''))
        rate_per_100000 = float(cells[2].text.replace(',', ''))
        women_prisoners = int(cells[3].text.replace(',', ''))
        percentage_women = float(cells[4].text.replace('%', ''))

        print(country, prison_population, rate_per_100000, women_prisoners, percentage_women)

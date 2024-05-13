import requests
from bs4 import BeautifulSoup
import pprint

url = "https://en.wikipedia.org/wiki/List_of_countries_by_incarceration_rate"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find the table with the incarceration rate data
table = soup.find("table", {"class": "wikitable"})

# Extract the table headers
headers = []
for th in table.find_all("th"):
    headers.append(th.text.strip())

# Extract the table rows
rows = []

for tr in table.find_all("tr")[2:]:
    row = {}
    tds = tr.find_all("td")
    row[headers[0]] = tds[0].text.strip()
    row[headers[1]] = tds[1].text.strip()
    row[headers[2]] = tds[2].text.strip()
    #row[headers[3]] = tds[3].text.strip()
    rows.append(row)

# Print the first row of data
pprint.pp(rows)
# https://stackoverflow.com/a/3075568/10051170
# https://pypi.org/project/beautifulsoup4/
# https://pypi.org/project/requests/
# https://toppornsites.com/

# scrape urls of porn sites from https://toppornsites.com/
# write them into sites.txt
# took cook from https://stackoverflow.com/a/3075568/10051170
# and made modifications to suite my needs

from bs4 import BeautifulSoup
import requests

URL = "https://toppornsites.com/"

html_page = requests.get(URL)
soup = BeautifulSoup(html_page.content, "html.parser")

with open("sites.txt", "w+") as ptr:
    for link in soup.findAll('a'):
        print(link.get('href'), file=ptr)

print("Done")

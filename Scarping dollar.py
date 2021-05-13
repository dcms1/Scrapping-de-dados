from bs4 import BeautifulSoup
from datetime import date
import requests


url = "https://dolarhoje.com/"

site = requests.get(url)

soup = BeautifulSoup(site.content, 'html.parser')
dollar_hoje = soup.find("input", id = "nacional").get("value")
data_hoje= date.today().strftime("%d/%m/%Y")
print("A cotação do dollar em {} é: R$ {}".format(data_hoje,dollar_hoje))

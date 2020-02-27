import requests
from bs4 import BeautifulSoup
import csv
#page = 1

response = requests.get("https://www.immoscout24.ch/en/house/rent/city-bern")
soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("article")

with open("immoscout.csv", "w", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["title", "url", "comment", "address", "price", "postal code"])

    for article in articles:
        a_tag = article.find_all("a")
        title = a_tag[0].get_text()
        url = a_tag[0]["href"]
        comment = article.find("h2").get_text()
        address = a_tag[1].get_text()
        postal_code = address[-13:-8] #address contains postal code
        price = article.find_all("h3")[1].get_text()[:-4] #price's string value has nonascii char
        #price = price[:-2]
        csv_writer.writerow([title, url, comment, address, price, postal_code])
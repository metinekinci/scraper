import requests
from bs4 import BeautifulSoup
import csv
page_counts = 1
response = requests.get("https://www.homegate.ch/rent/real-estate/city-bern/matching-list?")
soup = BeautifulSoup(response.text, "html.parser")
#a_tags = soup.find_all('a', {'data-test' : 'result-list-item'})
page_str = soup.find('nav', {'aria-label' : 'pagination'}).get_text()
if "..." in page_str:
    frst = page_str.find("...")
    page_counts = int(page_str[(frst+3):])
    print(page_counts)
else:
    page_counts = int(page_str[-1:])
with open("homegate.csv", "w", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["address", "price", "space"])
    for current_page in range(1,(page_counts + 1)):
        response = requests.get(f"https://www.homegate.ch/rent/real-estate/city-bern/matching-list?ep={current_page}")
        a_tags = soup.find_all('a', {'data-test' : 'result-list-item'})
#print(page_counts)
        for a in a_tags:
            p_tag = a.find_all("p")
            attrs = p_tag[0].get_text()
            address = p_tag[1].get_text()
            first_char = attrs.find('â')
            price = attrs[:(first_char - 1)]
            last_char = attrs.find('m')
            space = attrs[(first_char + 3):last_char]
            csv_writer.writerow([address, price, space])
        #print(price)
        #print(attrs)
        #print(address)
        #print(space)
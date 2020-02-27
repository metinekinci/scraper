import dryscrape
from bs4 import BeautifulSoup
session = dryscrape.Session()
session.visit("https://www.newhome.ch/fr/louer/recherche/maison-appartement/localite-bern/liste?wo=%5b%2210%3b470%22%5d")
response = session.body()
soup = BeautifulSoup(response)
soup.find(class_="col-xs-12 col-sm-8 details mobile-column-extendet")

from selenium import webdriver
driver = webdriver.PhantomJS()
driver.get(my_url)
p_element = driver.find_element_by_id(class_='col-xs-12 col-sm-8 details mobile-column-extendet')
print(p_element.text)

'''
from selenium import webdriver
driver = webdriver.PhantomJS()
driver.get("https://www.newhome.ch/fr/louer/recherche/maison-appartement/localite-bern/liste?wo=%5b%2210%3b470%22%5d")
p_element = driver.find_element_by_id(id_='intro-text')
print(p_element.text)
'''
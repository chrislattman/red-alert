from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("/usr/local/bin/chromedriver")

names=[]
phones=[]
addresses=[]

for i in range(1, 1682):
	counter = 1
	driver.get("https://www.rubmaps.ch/?i_agree_notice&to=%2Fadvanced-search-2694152-" + str(i))
	content = driver.page_source
	soup = BeautifulSoup(content, features="html.parser")
	for br in soup.findAll('br'):
		if counter > 27 and counter < 86:
			if counter % 4 == 0:
				addresses.append(br.nextSibling[16:].strip())
			if counter % 4 == 1:
				addresses[len(addresses) - 1] = addresses[len(addresses) - 1] + "; " + br.nextSibling[16:].strip()
		counter = counter + 1
	for a in soup.findAll('div', attrs={'class':'main-row'}):
		name = a.find('a', attrs={'class':'th-a'})
		phone = a.find('i', attrs={'class':'phonenumberrow'})
		names.append(name.text.strip())
		phones.append(phone.text.strip())

df = pd.DataFrame({'Parlor name':names,'Phone number':phones,'Address':addresses}) 
df.to_csv('massage_parlors.csv', index=False, encoding='utf-8')
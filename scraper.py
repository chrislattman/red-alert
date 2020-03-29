from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome("/usr/local/bin/chromedriver", options=options)

names = []
phones = []
addresses = []

for i in range(1, 1682):
	counter = 1
	driver.get("https://www.rubmaps.ch/?i_agree_notice&to=%2Fadvanced-search-2694152-" + str(i))
	content = driver.page_source
	soup = BeautifulSoup(content, features="html.parser")
	for br in soup.findAll('br'):
		if (i < 784 or i > 928) and i < 1556:
			if counter > 27 and counter < 86:
				if counter % 4 == 0:
					addresses.append(br.nextSibling[16:].strip())
				if counter % 4 == 1:
					addresses[len(addresses) - 1] = addresses[len(addresses) - 1] + "; " + br.nextSibling[16:].strip()
		elif (i > 784 and i < 928) or (i > 1556 and i != 1681):
			if counter > 27 and counter < 72:
				if counter % 3 == 1:
					addresses.append(br.nextSibling[16:].strip())
				if counter % 3 == 2:
					addresses[len(addresses) - 1] = addresses[len(addresses) - 1] + "; " + br.nextSibling[16:].strip()
		elif i == 928:
			if counter > 27 and counter < 60:
				if counter % 3 == 1:
					addresses.append(br.nextSibling[16:].strip())
				if counter % 3 == 2:
					addresses[len(addresses) - 1] = addresses[len(addresses) - 1] + "; " + br.nextSibling[16:].strip()
			if counter > 60 and counter < 76:
				if counter % 4 == 2:
					addresses.append(br.nextSibling[16:].strip())
				if counter % 4 == 3:
					addresses[len(addresses) - 1] = addresses[len(addresses) - 1] + "; " + br.nextSibling[16:].strip()
		elif i == 1681:
			if counter > 27 and counter < 48:
				if counter % 3 == 1:
					addresses.append(br.nextSibling[16:].strip())
				if counter % 3 == 2:
					addresses[len(addresses) - 1] = addresses[len(addresses) - 1] + "; " + br.nextSibling[16:].strip()
		elif i == 1556:
			if counter > 27 and counter < 46:
				if counter % 4 == 0:
					addresses.append(br.nextSibling[16:].strip())
				if counter % 4 == 1:
					addresses[len(addresses) - 1] = addresses[len(addresses) - 1] + "; " + br.nextSibling[16:].strip()
			if counter > 46 and counter < 76:
				if counter % 3 == 2:
					addresses.append(br.nextSibling[16:].strip())
				if counter % 3 == 0:
					addresses[len(addresses) - 1] = addresses[len(addresses) - 1] + "; " + br.nextSibling[16:].strip()
		else: #i == 784
			if counter > 27 and counter < 66:
				if counter % 4 == 0:
					addresses.append(br.nextSibling[16:].strip())
				if counter % 4 == 1:
					addresses[len(addresses) - 1] = addresses[len(addresses) - 1] + "; " + br.nextSibling[16:].strip()
			if counter > 66 and counter < 81:
				if counter % 3 == 1:
					addresses.append(br.nextSibling[16:].strip())
				if counter % 3 == 2:
					addresses[len(addresses) - 1] = addresses[len(addresses) - 1] + "; " + br.nextSibling[16:].strip()
		#print(br.nextSibling)
		#print(str(i) + ": " + str(counter))
		counter = counter + 1
	for a in soup.findAll('div', attrs={'class':'main-row'}):
		name = a.find('a', attrs={'class':'th-a'})
		phone = a.find('i', attrs={'class':'phonenumberrow'})
		names.append(name.text.strip())
		phones.append(phone.text.strip())
	#print(i)
	#print(str(i) + " " + str(len(names)) + " " + str(len(phones)) + " " + str(len(addresses)))
df = pd.DataFrame({'Parlor name':names,'Phone number':phones,'Address':addresses})
df.to_csv('massage_parlors.csv', index=False, encoding='utf-8')

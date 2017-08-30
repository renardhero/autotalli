from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

filename = "3_bemarit.csv"
f = open(filename, "w")
headers = "otsikko, hinta, ajettu, vuosimalli\n"
f.write(headers)

my_urls = []
for i in range(0,60):
	my_urls.append('http://www.autotalli.com/vaihtoautot/listaa/BMW/3-sarja/sivu/' + str(i))

for my_url in my_urls:
	uClient = uReq(my_url)
	page_html = uClient.read()
	page_soup = soup(page_html, "html.parser")
	containers = page_soup.findAll("div", {"class":"listRow"})

	for container in containers:
		
		container1 = container.findAll("div", {"class":"carsListItemCarNameContainer"})
		otsikko = container1[0].a.text
		
		container2 = container.findAll("div", {"class":"carsListItemCarDetailBottomContainer"})
		hinta = container2[0].div.div.text
		
		container3 = container2[0].findAll("div", {"class":"usedCarsListItemCarMeterReading"})
		ajettu = container3[0].div.text
		
		container4 = container2[0].findAll("div", {"class":"usedCarsListItemCarModelYear"})
		vuosimalli = container4[0].div.text

		f.write(otsikko.replace(",",".") + "," + hinta + "," + ajettu + "," + vuosimalli + "\n")

f.close()
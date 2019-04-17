from datetime import date
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
current_date = date.today()
filename="results {}_{}_{}.csv".format(current_date.day, current_date.month, current_date.year)
f=open(filename,"w")
headers="suburb,address,bed,result,price,link\n"
f.write(headers)
all_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o","p","q","r","s","t","u","v", "w", "x", "y", "z"]
for letter in all_letters:
	RE_url = 'https://www.realestateview.com.au/sales-and-auction-results/victoria/'+letter+'/'
	# opens a connection to URL
	uClient = uReq(RE_url)
	# puts all the HTML into a container
	page_html = uClient.read()
	# closes connection
	uClient.close()
	# stores html as soup
	page_soup = soup(page_html, "html.parser")

	#finds relevant info on page
	containers=page_soup.findAll("tr",{"class":"auction-result-item"})


	#things you want: Suburb, address, bedrooms, result, price
	for container in containers:
		#suburb
		suburb_container=container.findAll("meta",{"itemprop":"addressLocality"})
		suburb=suburb_container[0].get("content")
		#Address
		address_container=container.findAll("span",{"itemprop":"streetAddress"})
		address = address_container[0].text
		#number of bedrooms
		bedroom_container=container.findAll("td",{"class":"bedroom hidden-xs"})
		bedroom=bedroom_container[0].text
		#sold result
		result_container = container.findAll("td",{"class":"sale-type hidden-xs"})
		result=result_container[0].text
		#Price
		price_container = container.findAll("td",{"class":"price hidden-xs"})
		price=price_container[0].text
		#hyperlink
		link_container = container.findAll("a",{"target":"_blank"})
		if link_container == []:
			link = "-"
		else:
			link = link_container[0].get("href")
		price=price.replace("$",'')
		price=price.replace(",", '')
		if price == "undisclosed":
			price = ''
		f.write(suburb.replace(" ",'')+","+address.replace(",", "|")+","+bedroom+","+result+","+price+ "," + link + "\n")

f.close()

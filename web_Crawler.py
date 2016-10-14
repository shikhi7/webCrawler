import requests

seedPage = raw_input('Enter the link of your seed page link: ')   #determines the link to start crawling from
links = [seedPage]	#list containing all the links
countOnLinks=1	#keeps count on total count of entries in 'links' list
indexOfCurrentLink=0	#stores the index of the link (in 'links' list) that is currently being crawled

while True:
	try:
		thresholdNumber = int(raw_input('Enter your threshold number: '))   #determines the number of links starting from index 0 that will be crawled.
	except ValueError:
		print("Enter a valid positive integer")

def crawl(sourceCode):
	next_link = getNextTarget(sourceCode)
	if (next_link==''):
		indexOfCurrentLink += 1
		crawl(getPage(links[i]))
	else:
		if next_link in links:
			crawl(sourceCode[(next_link[1]):])
		else:
			links.append(next_link)
			countOnLinks += 1
			crawl(sourceCode[(next_link[1]):])


#function to extract the source code from its link
def getPage(pageLink):
	return requests.get(pageLink)

def getNextTarget(sourceCode):
	startLink = sourceCode.find("<a href=") + 9	  #starting index of the new link
	endLink = sourceCode.find('"', startLink)   #ending index of the new link
	return sourceCode[startLink:endLink]

# main program starts from here-

seedPageSource = getPage(seedPage)
crawl(seedPage)


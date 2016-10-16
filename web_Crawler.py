import requests

seedPage = raw_input('Enter the link of your seed page link: ')   #determines the link to start crawling from
links = [seedPage]	#list containing all the links
countOnLinks=1	#keeps count on total count of entries in 'links' list
indexOfCurrentLink=0	#stores the index of the link (in 'links' list) that is currently being crawled
searchContent = {}   #dictionary that stores keywords of search as keys and list of links whose sourcecode had its mention as value.

while True:
	try:
		thresholdNumber = int(raw_input('Enter your threshold number: '))   #determines the number of links starting from index 0 that will be crawled.
		break
	except ValueError:
		print("Enter a valid positive integer")

#defining functipons-

def crawl(sourceCode):
	next_link = getNextTarget(sourceCode)
	if (next_link==''):
		indexOfCurrentLink += 1
		crawl(getSource(links[i]))
	else:
		if next_link in links:
			crawl(sourceCode[(next_link[1]):])
		else:
			links.append(next_link)
			countOnLinks += 1
			crawl(sourceCode[(next_link[1]):])

def getSource(pageLink): #function to extract the source code from its link
	return requests.get(pageLink)

def getNextTarget(sourceCode):
	startLink = sourceCode.find("<a href=") + 9	  #starting index of the new link
	endLink = sourceCode.find('"', startLink)   #ending index of the new link
	return sourceCode[startLink:endLink]

def updateDictionary(pageLink, searchContent):    #this function updates keywords of a particular page source provided by the page link.
	sourcecode = getSource(pageLink)
	wordsList = sourceCode.split()
	for word in wordsList:
		if (word in searchContent.keys()):
			(searchContent['word']).append(pageLink)
		else:
			searchContent.update({'word':[]})
			(searchContent['word']).append(pageLink)

# main program starts from here-

while (indexOfCurrentLink < thresholdNumber) :
	crawl(getSource(links[indexOfCurrentLink]))
	updateDictionary(links[indexOfCurrentLink], searchContent)
	indexOfCurrentLink += 1

query = raw_input("Enter your search query: ")
resultLinks = []

queryWords = query.split()
for word in queryWords:
	if (word in searchContent.keys()):
		for relatedLinks in searchContent['word']:
			resultLinks.append(relatedLinks)
	else:
		continue

if (resultLinks != []):
	for results in resultLinks:
		print(results)
else:
	print("No results found")
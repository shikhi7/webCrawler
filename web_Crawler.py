import requests

links = []
i=0
seedpage = raw_input('Enter the link of your seed page:')

def crawl(sourceCode):
	next_link = getNextTarget(sourceCode)
	if (next_link==''):
		i = i+1
		crawl(getPage(links[i]))
	else:
		if next_link in links:
			crawl(sourceCode[(next_link[1]):])
		else:
			links.append(next_link)
			crawl(sourceCode[(next_link[1]):])


def getPage(pageLink):
	return requests.get(pageLink)

def getNextTarget(sourceCode):
	startLink = sourceCode.find("<a href=") + 9
	endLink = sourceCode.find('"', startLink)
	return sourceCode[startLink:endLink]
	
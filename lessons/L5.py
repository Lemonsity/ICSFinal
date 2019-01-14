#Web Scrapping
#The fifth tutorial of PYTeach revolves around getting a list of grammer
#Todo this we must gather words from a website


#Import Beautiful soup and requests
import requests
from bs4 import BeautifulSoup
#Request website to get grammer from
r = requests.get("https://www.vocabulary.com/lists/290105")

#Make soup
soup = BeautifulSoup(r.content, 'html.parser')

#<li class="entry" id="entry1"
# lang="en" word="abacinate" freq="∞" prog="">

#Go through each tag based on website, this is where the word is stored
inputTag = soup.find_all("li", {"class": "entry"}, {"word"})

#Write to a file
for i in range(500):
	f = open("data.txt", "a")
	x = inputTag[i].get('word')
	f.write("\n '" + x + "',")

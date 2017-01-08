
# scrape natgeo to pull the photo of the day and set as desktop background

from bs4 import BeautifulSoup
import urllib.request
import re
import datetime
import os.path


class ScrapeWebpage:

	def __init__(self, directory, filename, url):
		'''
		directory: string of directory to save image i.e., C:/Users/UserX/Documents
		filename: string of filename to save image as; automatically appends a timestamp
		url: string of website to scrape
		'''
		self.setDirectory(directory)
		self.setFilename(filename)
		self.setUrl(url)

	def setDirectory(self, directory):
		'''
	    Test if directory is valid and change working directory to directory
		'''
		if os.path.isdir(directory):
			print("Changing directory for file save location to {}".format(directory))
			self.directory = directory
		else:
			print("{} is not a valid directory.".format(directory))

	def setUrl(self, url):
		''' Set the url. Pass as string'''
		try:
			self.url = url
			self.setHtml(url)
		except urllib.request.URLError:
			print("{} is not a valid url; cannot connect to address".format(url))

	def setHtml(self, url):
		''' 
		Pass an url as a string to return the html of the webpage.
		Returns html in string output.
		'''
		if url == self.url:
			print("Getting html of {}\n".format(url))
		else:
			print("Updating url to {}".format(url))
			print("Getting html of {}\n".format(url))
			self.url = url
		self.html = BeautifulSoup(urllib.request.urlopen(url))
	

	def getTags(self, tagString):
		'''
		Pass string from html of webpage and tag to pull from html.
		Returns string array of all <> with tag.
		'''

		print("Searching for tag <{}> in html...".format(tagString))
		tags = self.html.find_all(tagString)
		if not tags:
			print("No tags found for <{}> in html".format(tagString))
		else:
			print("Tags found, Updating html...\n")
			self.html = tags

	def extractHtml(self, reText):
		'''
		Pass string matchString to be parsed and string reText to find match.
		Note: reText must be in regular expression format.
		Returns first match.
		'''

		match = re.search(reText, str(self.html))
		# catch error if no match found
		if match is None:
			print("'{}' regular expression not found in '{}'\n".format(reText, self.html))
			return
		# else set first match as html
		else:
			print("Match found, updating html...\n".format(match.group(0)))	
			self.setHtml(match.group(0))

	def setFilename(self, filename, addTimestamp=True):
		self.filename = filename
		if addTimestamp:
			today = self.getTimestamp()
		# append timestamp and save as .jpg
		self.filename += today
		self.filename += '.jpg'

	def getTimestamp(self):
		today = datetime.datetime.now()
		day, month, year = today.day, today.month, today.year
		# conserve leading zeroes
		day = str('0' + str(day))[-2:]
		month = str('0' + str(month))[-2:]
		year = str(year)[-2:]
		timestamp = day + month + year
		return(timestamp)

	def saveImage(self):
		'''
		Saves image in directory with name filename. 
		Be sure directory, filename, and a valid url are set.
		'''

		if None in {self.directory, self.filename, self.url}:
			print("Make sure you set directory, filename, and url before saving")
			return

		# save image at filepath
		filepath = os.path.join(self.directory, self.filename)
		img = urllib.request.urlretrieve(self.url, filepath)
		# show where image is saved
		print("saving {}...".format(img))

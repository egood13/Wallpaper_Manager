
# WORK IN PROGRESS

import os
import datetime
import time

class FileManager:

	def __init__(self):
		pass

	def setDirectory(self, directory):
		if os.path.isdir(directory):
			self.directory = directory
			os.chdir(directory)
		else:
			print("{} is not a valid directory.".format(directory))
			

	def fileList(self):
		pass

	def lastModified(self):
		pass

	def lastFile():
		pass





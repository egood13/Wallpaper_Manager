
import os
import ctypes

class SetBackground:

	def __init__(self, directory, filename):
		'''
		Initialize and test if directory and filename are valid.
		If valid, set as desktop background
		'''
		if os.path.isdir(directory):
			print("Setting directory to {}".format(directory))
			self.directory = directory
			os.chdir(directory)
		else:
			print("{} is not a valid directory. Please try again.".format(directory))
			return
		print(os.path.join(directory, filename))
		if os.path.isfile(filename):
			print("Getting {} from {}...".format(filename, directory))
			self.filename = filename
		else:
			print("{} does not exist in {}".format(filename, directory))
			return
		
		self._setBackground()

	def _setBackground(self):
		'''
		Set image saved under filename in directory to desktop background.
		Must use saveImage first
		'''
		SPI_SETDESKWALLPAPER = 20
		filepath = os.path.join(self.directory, self.filename)
		print("Setting {} as background... ".format(self.filename))
		ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, filepath, 3)


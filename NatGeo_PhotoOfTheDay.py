
'''
Use ScrapeWebpage to save the National Geographic photo of the day and 
SetBackground to set the image as the desktop background
'''
import ScrapeWebpage as sw
import SetBackground as sb

def main():

	natgeoUrl = 'http://photography.nationalgeographic.com/photography/photo-of-the-day/'

	natgeo = sw.ScrapeWebpage(directory='C:\\Users\\Elliott\\Pictures\\Wallpapers',
						      filename='natgeo_photo-of-the-day',
							  url=natgeoUrl) # initialize scraper
	# natgeo's photo of the day reroutes the browser to a slideshow of pictures
	natgeo.getTags("link")									# search link tags to navigate to the first photo of the slideshow
	natgeo.extractHtml('http\S+photo-of-the-day\S+/')
	
	natgeo.getTags("meta")
	natgeo.extractHtml('http://yourshot\S+/')				# extract photo link
	# save image and set as desktop background
	natgeo.saveImage()
	setImage = sb.SetBackground(directory=natgeo.directory, filename=natgeo.filename)

if __name__ == '__main__':
	main()
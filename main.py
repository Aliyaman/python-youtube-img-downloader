import youtube_dl
from selenium import webdriver

#Profile link or video link
#Read documentation.
url = ""#Enter url here.

#Starts Firefox webdriver.
#It is necessary to start Firefox webdriver
driver = webdriver.Firefox()
driver.set_window_size(600,600)

#All possible functions to use

#youtube_dl.profile_pic_downloader(url, driver)
#youtube_dl.banner_downloader(url,driver)
#youtube_dl.download_thumbnail(url,driver)
#youtube_dl.download_community_post(url, driver)
import youtube_dl
from selenium import webdriver

url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

driver = webdriver.Firefox()
driver.set_window_size(600,600)

#All possible functions to use

#youtube_dl.profile_pic_downloader(url, driver)
#youtube_dl.banner_downloader(url,driver)
#youtube_dl.download_thumbnail(url,driver)
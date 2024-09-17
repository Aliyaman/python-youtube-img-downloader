import youtube_dl
from selenium import webdriver

#url = "https://www.youtube.com/@testotaylan"
url = "https://www.youtube.com/watch?v=_ksoWeZdG54"

driver = webdriver.Firefox()
driver.set_window_size(600,600)

#youtube_dl.profile_pic_downloader(url, driver)
#youtube_dl.banner_downloader(url,driver)
youtube_dl.download_thumbnail(url,driver)
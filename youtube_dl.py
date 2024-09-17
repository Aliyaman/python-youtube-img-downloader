from selenium.webdriver.common.by import By
from time import sleep
from download_image import downloader


def profile_pic_downloader(url, driver):
    #downloads channel profile pic
    file_name = url.split("@")[1]
    driver.get(url)
    sleep(5)
    img_url = driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/div[3]/ytd-tabbed-page-header/tp-yt-app-header-layout/div/tp-yt-app-header/div[2]/div/div[2]/yt-page-header-renderer/yt-page-header-view-model/div/div[1]/yt-decorated-avatar-view-model/yt-avatar-shape/div/div/div/img").get_attribute("src")
    downloader(img_url, file_name)
    driver.quit()

def banner_downloader(url, driver):
    #downloads channel banner
    file_name = url.split("@")[1] + "_banner"
    driver.get(url)
    sleep(5)
    img_url = driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/div[3]/ytd-tabbed-page-header/tp-yt-app-header-layout/div/tp-yt-app-header/div[2]/div/div[1]/div/yt-image-banner-view-model/img").get_attribute("src")
    downloader(img_url, file_name)
    driver.quit()

def download_thumbnail(url, driver):
    #download video thumbnail
    file_name = url.split("=")[1]
    driver.get(url)
    sleep(5)
    img_url = driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[7]/div").get_attribute("outerHTML")
    #extract url from code
    start_style = img_url.find('style="') + len('style="')
    end_style = img_url.find('";', start_style)
    style_value = img_url[start_style:end_style]
    url_start = style_value.find('url(&quot;') + len('url(&quot;')
    url_end = style_value.find('&quot;', url_start)
    url = style_value[url_start:url_end]
    print(url)
    downloader(url, file_name)
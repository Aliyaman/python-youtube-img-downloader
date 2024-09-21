from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from time import sleep
from download_image import downloader


def profile_pic_downloader(url, driver):
    #downloads channel profile pic
    file_name = url.split("@")[1]
    driver.get(url)
    sleep(5)
    img_url = driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/div[3]/ytd-tabbed-page-header/tp-yt-app-header-layout/div/tp-yt-app-header/div[2]/div/div[2]/yt-page-header-renderer/yt-page-header-view-model/div/div[1]/yt-decorated-avatar-view-model/yt-avatar-shape/div/div/div/img").get_attribute("src")
    downloader(img_url, file_name)
    sleep(2)
    driver.quit()

def banner_downloader(url, driver):
    #downloads channel banner
    file_name = url.split("@")[1] + "_banner"
    driver.get(url)
    sleep(5)
    img_url = driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/div[3]/ytd-tabbed-page-header/tp-yt-app-header-layout/div/tp-yt-app-header/div[2]/div/div[1]/div/yt-image-banner-view-model/img").get_attribute("src")
    downloader(img_url, file_name)
    sleep(2)
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
    sleep(2)
    driver.quit()

def download_community_post(url, driver):
    #This funcion downloads pictures shared in Youtube community post
    file_name = url[90:]
    driver.get(url)
    sleep(5)
    img_url = driver.find_element(By.CSS_SELECTOR,"ytd-backstage-image-renderer.style-scope:nth-child(1) > div:nth-child(2) > yt-img-shadow:nth-child(1) > img:nth-child(1)").get_attribute("src")
    downloader(img_url,file_name)
    sleep(2)
    print(f"Image downloaded as: {file_name}.jpg")
    try:
        #is there second image
        right_arrow = driver.find_element(By.XPATH,"""//*[@id="right-arrow"]""")
        right_arrow.click()
        img_url = driver.find_element(By.CSS_SELECTOR,"ytd-backstage-image-renderer.style-scope:nth-child(2) > div:nth-child(2) > yt-img-shadow:nth-child(1) > img:nth-child(1)").get_attribute("src")
        downloader(img_url,file_name+"2")
        sleep(2)
        print(f"Image downloaded as: {file_name}2.jpg")
    except NoSuchElementException:
        pass
    except ElementNotInteractableException:
        pass

    try:
        #is there third image
        right_arrow = driver.find_element(By.XPATH,"""//*[@id="right-arrow"]""")
        right_arrow.click()
        img_url = driver.find_element(By.CSS_SELECTOR,"ytd-backstage-image-renderer.style-scope:nth-child(3) > div:nth-child(2) > yt-img-shadow:nth-child(1) > img:nth-child(1)").get_attribute("src")
        downloader(img_url,file_name+"3")
        sleep(2)
        print(f"Image downloaded as: {file_name}3.jpg")
    except NoSuchElementException:
        pass
    except ElementNotInteractableException:
        pass

    try:
        #is there fourth image
        right_arrow = driver.find_element(By.XPATH,"""//*[@id="right-arrow"]""")
        right_arrow.click()
        img_url = driver.find_element(By.CSS_SELECTOR,"ytd-backstage-image-renderer.style-scope:nth-child(4) > div:nth-child(2) > yt-img-shadow:nth-child(1) > img:nth-child(1)").get_attribute("src")
        downloader(img_url,file_name+"4")
        sleep(2)
        print(f"Image downloaded as: {file_name}4.jpg")
    except NoSuchElementException:
        pass
    except ElementNotInteractableException:
        pass

    try:
        #is there fifth image
        right_arrow = driver.find_element(By.XPATH,"""//*[@id="right-arrow"]""")
        right_arrow.click()
        img_url = driver.find_element(By.CSS_SELECTOR,"ytd-backstage-image-renderer.style-scope:nth-child(5) > div:nth-child(2) > yt-img-shadow:nth-child(1) > img:nth-child(1)").get_attribute("src")
        downloader(img_url,file_name+"5")
        sleep(2)
        print(f"Image downloaded as: {file_name}5.jpg")
    except NoSuchElementException:
        pass
    except ElementNotInteractableException:
        pass
    driver.quit()
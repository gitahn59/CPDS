from selenium import webdriver

from PIL import Image
from io import  BytesIO

import urllib.request
import os
import time
import requests

def GetImages(searchTerm, count):
    url = "https://www.google.com/search?q=" + searchTerm + "&source=lnms&tbm=isch"
    browser = webdriver.Chrome('C:/chromedriver_win32/chromedriver.exe')
    browser.get(url)
    src_list = []
    succount = 0

    header = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}

    if not os.path.exists('Image/' + searchTerm):
        try:
            os.makedirs('Image/' + searchTerm)
        except OSError:
            print("Error : Creating Directory. ")
            return

    download_path = 'Image/' + searchTerm + '/'
    #scrolling
    for _ in range(1,5):
        for _ in range(1000):
            browser.execute_script('window.scrollBy(0,10000)')
        try:
            browser.find_element_by_class_name("mye4qd").click()
        except:
            time.sleep(1)

    for x in browser.find_elements_by_class_name('rg_i'):
        src = x.get_attribute('src')
        if src != None:
            image_name = download_path + searchTerm + "_" + str(succount) + '.jpg'
            urllib.request.urlretrieve(src, image_name)

            original_image = Image.open(image_name)
            resize_image = original_image.resize((1024, 600))
            resize_image.save(image_name, quality=95)
            succount = succount + 1

            print(image_name, "succesfully downloaded")
            # src_list.append(src)

            if succount > count:
                break

    print(succount, "succesfully downloaded")
    browser.close()

if __name__ == '__main__' :
    GetImages('crosswalk', 1000)
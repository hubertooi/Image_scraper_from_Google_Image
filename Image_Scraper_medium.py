# Libraries
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
import time

img_name = 'new years day' # image object name
number_imgs = 5 # number of images wanted
delay = 2 # time delay in seconds

# get the path for chromedriver
# this just make it easy for user to download the chromedrive.exe to the same main folder with the python code
here = os.path.abspath(__file__)
input_dir = os.path.abspath(os.path.join(here, os.pardir))
chromeDriverPath = os.path.join(input_dir, 'chromedriver.exe')

#######################################################################################################################
# creating a directory to save images
folder_name = f'{img_name} imgs'
if not os.path.isdir(folder_name): # if the folder name "image name" imgs
    os.makedirs(folder_name) # it creates the folder

#######################################################################################################################
# download function
# input parameters are url, folder name, image counter
# this function check urls if it is fine to download the images
def download_image(url, folder_name, num):
    try:
        image_content = requests.get(url).content
    except Exception as e:
        print(f'Error - Could not download {url} - {e}')
    
    try:
        f = open(os.path.join(folder_name, str(num)+".jpg"), 'wb')
        f.write(image_content)
        f.close()
        print(f"Success - saved {url}")
    except Exception as e:
        print(f"Error - Could not save {url}-{e}")

#######################################################################################################################
# web function for webdriver
def web():
    s=Service(chromeDriverPath) # service 
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging']) # remove devtool message
    options.add_experimental_option('detach',True) # make sure the web browser stay open
    wd = webdriver.Chrome(service=s, options=options) # opening chrome driver
    return wd

wd = web() # create an instance of the webdriver 

# #######################################################################################################################
# Function to extract image urls
# input parameters are image name, max number of url needed, and time delay in seconds
# function returns a set of image urls
def fetch_image_urls(img_name, max_url,time_delay):
    
    # Function to scroll to end
    def scroll_to_end(wd):
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(time_delay)

    search_url = f"https://www.google.com/search?q={img_name}&source=lnms&tbm=isch"
    wd.get(search_url)

    image_urls = set()
    image_count = 0
    results_start = 0

    while image_count < max_url:
        scroll_to_end(wd)

        thumbnail_results = wd.find_elements(By.CLASS_NAME,"Q4LuWd")
        number_results = len(thumbnail_results)

        for img in thumbnail_results[results_start:number_results]:
            try:
                img.click()
                time.sleep(time_delay)
            except Exception:
                continue

            actual_images = wd.find_elements(By.CLASS_NAME,'n3VNCb')
            for actual_image in actual_images:
                if actual_image.get_attribute('src') and 'http' in actual_image.get_attribute('src'):
                    image_urls.add(actual_image.get_attribute('src'))

            image_count = len(image_urls)

            if len(image_urls) >= max_url:
                print(f"Found:{len(image_urls)} image links, done!")
                break

        else:
            print(f"Found: , {len(image_urls)}, image links, looking for more ...")
            time.sleep(30)
            load_more_button = wd.find_elements(By.CSS_SELECTOR,".mye4qd")
            if load_more_button:
                wd.execute_script("document.querySelector('.mye4qd').click();")
        
        results_start = len(thumbnail_results)

    return(image_urls)

# #######################################################################################################################
# using the fetch_image_urls and store the urls as img_urls
img_urls = fetch_image_urls(img_name, number_imgs, delay)
wd.quit() # quit webdrive

# #######################################################################################################################
# simple counter with a for loop to download image and save it as the counter number.jpg
counter = 0
for i in img_urls:
    print(i)
    download_image(i,folder_name,counter)
    print(f'Downloaded img {counter} of url {i}\n')
    counter += 1
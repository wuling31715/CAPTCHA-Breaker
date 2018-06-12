from selenium import webdriver
from time import sleep
from PIL import Image
from io import BytesIO
import os

# set up some variable
start_url = "http://railway.hinet.net/Foreign/TW/etkind1.html"
id = "F129525019"
count = 831

# open browser and make windows to max
browser = webdriver.Chrome('/Users/wangboren/python3/semester_project/machine_learning_PG/chromedriver')
browser.set_window_position(0,0)
browser.set_window_size(1680,2169.800)
browser.get(start_url)

# login to captcha pics page
browser.find_element_by_id('person_id').send_keys(id)

# sleep for few seconds
# in order to avoid block by google or soome kinds
sleep(5)

# after filling in the blank
# click submit button
browser.find_element_by_css_selector("button[type='submit']").click()

# sleep for few seconds
# in order to avoid block by google or soome kinds
sleep(5)

# create directory if not exsist
# put image in < captcha-photos-remain > dir
if not os.path.exists("captcha-photos-second"): 
    os.mkdir("captcha-photos-second")

# put image in < captcha-photos-first > dir
# if not os.path.exists("captcha-photos-first"): 
#     os.mkdir("captcha-photos-first")

while(count<=10000) :
    # get captcha img and get its size and location
    captcha_img_element = browser.find_element_by_id("idRandomPic")
    captcha_img_element_location = captcha_img_element.location
    captcha_img_element_size = captcha_img_element.size

    # change to image
    captcha_img = browser.get_screenshot_as_png()
    final_captcha_img = Image.open(BytesIO(captcha_img))

    # sleep for few seconds
    # in order to avoid block by google or soome kinds
    sleep(5)

    # defines crop points , and saves new cropped image
    final_captcha_img = final_captcha_img.crop((760, 920, 1160, 1040))
    print(count) 
    final_captcha_img.save('captcha-photos-remain/第{}張圖片.png'.format(count)) 

    # sleep for few seconds
    # in order to avoid block by google or soome kinds
    sleep(5)

    # find 「 重新產生驗證碼 」button
    browser.find_element_by_xpath("/html/body/div/div[3]/div/form/div/div[1]/button[2]").click()

    # sleep for few seconds
    # in order to avoid block by google or soome kinds
    sleep(5)
    
    # finish forloop
    count = count + 1






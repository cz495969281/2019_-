import time

from selenium import webdriver

brower = webdriver.Chrome()
brower.implicitly_wait(10)

brower.get("https://accounts.douban.com/login")

brower.find_element_by_id("email").send_keys("13641112526")
brower.find_element_by_id("password").send_keys("chenze24")

brower.find_element_by_name("login").submit()

time.sleep(5)

brower.quit()
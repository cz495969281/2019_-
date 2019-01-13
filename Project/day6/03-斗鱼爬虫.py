import time

from selenium import webdriver


#导入定义
from selenium.webdriver.common.by import By

# 延迟等待对象
from selenium.webdriver.support.ui import WebDriverWait

#条件对象
from selenium.webdriver.support import expected_conditions as ec



browser = webdriver.Chrome()

browser.get("https://www.douyu.com/directory/all")

# browser.implicitly_wait(10)


while True:
    time.sleep(1)
    #创建延迟对象，实现对单个元素进行等待
    wait = WebDriverWait(browser,10)

    #出现页面没有加载完成就获取数据

    # a_tag_list = browser.find_elements_by_xpath('//a[@class="play-list-link"]')
    # print(a_tag_list)

    a_tag_list = wait.until(
        ec.presence_of_all_elements_located((By.XPATH,'//a[@class="play-list-link"]'))
    )

    for a_tag in a_tag_list:
        item = {}
        title = a_tag.find_element_by_css_selector(".ellipsis")
        item["title"] = title.text if title is not None else ""
        author = a_tag.find_element_by_css_selector(".dy-name.ellipsis.fl")
        item["author"] = author.text if author is not None else ""
        img  = a_tag.find_element_by_css_selector(".JS_listthumb")
        item["img"] = img.get_attribute("data-original") if img is not None else ""

        print(item)
    try:
        browser.find_element_by_class_name("shark-pager-next").click()
        print("下一页")
    except:
        pass

browser.quit()
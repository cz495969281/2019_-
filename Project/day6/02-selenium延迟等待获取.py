from selenium import webdriver
import time

#导入定义
from selenium.webdriver.common.by import By

# 延迟等待对象
from selenium.webdriver.support.ui import WebDriverWait

#条件对象
from selenium.webdriver.support import expected_conditions as ec



#创建浏览器对象
# 创建chrome浏览器
# 加载驱动 2种方案
#   第一种：直接通过路劲取加载驱动文件
#   第二种：path环境变量自动寻找

#通过驱动取创建浏览器对象
browser = webdriver.Chrome()


#设置超时时间，加载网页10秒之内,如果超过10秒还没有加载就超时
# browser.implicitly_wait(10)

#输入网址访问
browser.get("http://www.baidu.com")

browser.find_element_by_id("kw")

#创建延迟对象
wait = WebDriverWait(browser,10)

#等待元素 ID = "kw" 直到找到才返回
input = wait.until(
    ec.presence_of_all_elements_located((By.ID,"kw"))
)

#执行js代码
# browser.execute_script("var input = document.getElementById('kw');input.style.border='red solid 2px'")

time.sleep(10)

browser.quit()
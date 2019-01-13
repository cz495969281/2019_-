from selenium import webdriver
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()
url = "https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"

browser.get(url)
browser.switch_to.frame('iframeResult')
source = browser.find_element_by_css_selector('#draggable')
target = browser.find_element_by_css_selector('#droppable')
actions = ActionChains(browser)
actions.drag_and_drop(source,target)

# 执行链中的所有动作
actions.perform()

# ActionChains的执行原理，当你调用ActionChains的方法时，不会立即执行，
# 而是会将所有的操作按顺序存放在一个队列里，当你调用perform()方法时，队列中的时间会依次执行

"""
switch_top

alert ——返回浏览器的Alert对象，可对浏览器alert、confirm、prompt框操作

default_content() ——切到主文档

frame(frame_reference) ——切到某个frame

parent_frame() ——切到父frame，这个方法也不常被人所知，但有多层frame的时候很有用，不过这里要提一句，一般这种嵌套多层的frame都是有问题的，会影响到性能，可以提给开发，让其改进 
window(window_name) ——切到某个浏览器窗口 
active_element ——返回当前焦点的WebElement对象
"""
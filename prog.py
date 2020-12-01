from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Firefox(executable_path='./geckodriver.exe')

# open web page
driver.get('https://apress.com')

# maximize windows
driver.maximize_window()

# fullScreen
driver.fullscreen_window()

# set windows size
driver.set_window_size(800, 800)

# set windows position
driver.set_window_position(x=500, y=400)

# set window size with co-ordinate
driver.set_window_rect(x=30, y=30, width=450, height=500)

# get window positon
pos = driver.get_window_position()

# get windows size
driver.get_window_size()

# driver.close()
driver.quit()

# go back to previous page
driver.back()

# go to forward page
driver.forward()

# page refresh
driver.refresh()


# MOUSE CLICK
driver.find_element_by_id('id').click()

# MOUSE CLICK AND HOLD
button = driver.find_element_by_id('id')
webdriver.ActionChains(driver).click_and_hold(button).perform()

# MOUSE CONTEXT CLICK
button = driver.find_element_by_id('id')
webdriver.ActionChains(driver).context_click(button).perform()

# MOUSE DOUBLE CLICK
button = driver.find_element_by_id('id')
webdriver.ActionChains(driver).double_click(on_element=button).perform()

# MOUSE MOVE TO AN ELEMENT
menu = driver.find_element_by_id('id')
webdriver.ActionChains(driver).move_to_element(menu).perform()

# wait for sub menu to be displayed
WebDriverWait(driver, 3).until(
    EC.visibility_of_element_located((By.LINK_TEXT, "python")))
submenu = driver.find_element_by_link_text('python')
submenu.click()

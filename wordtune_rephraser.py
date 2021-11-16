from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from dotenv import load_dotenv
import os
from time import sleep


load_dotenv()

my_email = os.getenv('EMAIL')
my_password = os.getenv('PASSWORD')
chrome_driver_path = os.getenv('CHROME_DRIVER_PATH')


def rephraser(docs_url):
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    driver.maximize_window()
    driver.get(docs_url)
    action = ActionChains(driver)
    action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
    action.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
    sleep(5)
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get('https://app.wordtune.com/login')
    email = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@name="email"]')))
    email.send_keys(my_email)
    password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@name="password"]')))
    password.send_keys(my_password)
    login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, '//button[@data-testid="login_button"]')))
    login_button.click()
    sleep(5)
    driver.get('https://app.wordtune.com/editor')
    try:
        welcome_window = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '//body/div[3]/div[3]/div/div/div/div[1]/div[4]')))
    except TimeoutException as e:
        welcome_window = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '//body/div[4]/div[3]/div/div/div/div[1]/div[4]')))
    welcome_window.click()
    editor = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, '//div[@id="editorContentEditable"]')))
    editor.send_keys(Keys.CONTROL, 'v')
    sleep(2)
    # child_elements_p = editor.find_elements_by_xpath('//p/span')
    # child_elements_h2 = editor.find_elements_by_xpath('//h2/span')
    # child_elements_h3 = editor.find_elements_by_xpath('//h3/span')
    child_elements_p = editor.find_elements_by_tag_name('p')
    child_elements_h2 = editor.find_elements_by_tag_name('h2')
    child_elements_h3 = editor.find_elements_by_tag_name('h3')
    child_elements = child_elements_p + child_elements_h3 + child_elements_h2


    for child in child_elements:
        driver.execute_script(
            'arguments[0].scrollIntoView({block: "center", inline: "center"})', child)
        a = ActionChains(driver)
        a.move_to_element(child)
        driver.switch_to_active_element
        sleep(1)
        for i in range(3):
            a.click()
        a.perform()
        rewrite_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '//button[@data-testid="editorToolbarButtonRewrite"]')))
        rewrite_button.click()
        # a.key_down(Keys.CONTROL).send_keys('d').key_up(Keys.CONTROL).perform()
        for i in range(100000):
            try:
                first_div = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                    (By.XPATH, '//div[@data-testid="RewriteBox"]/div[1]/div[1]')))
                first_div.click()
                sleep(1)
            except TimeoutException as e:
                break
        driver.execute_script(js,child)

    editor.send_keys(Keys.CONTROL, 'a')
    editor.send_keys(Keys.CONTROL, 'c')
    sleep(1)
    driver.switch_to.window(driver.window_handles[0])
    sleep(3)
    a = ActionChains(driver)
    a.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
    a.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
    sleep(20)


docs_url = "https://docs.google.com/document/d/1fqQ6U9f5wXMX0qL3p4OjEor7D7dtZtB0xXCM_ouP5NQ/edit#"
w = rephraser(docs_url)


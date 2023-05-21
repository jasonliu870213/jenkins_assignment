import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def test_page():
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get('http://54.201.140.239/')
    logging.info('go to site')
    wait = WebDriverWait(driver, 3)  # Set wait time
    path = '//a[@href="./index.html"]'


    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, path)))
        # wait.until(EC.presence_of_element_located((By.XPATH, '//img[@class="product__image"]')))
        time.sleep(5)
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    except Exception:
        logging.info('FAILQQ')
        assert False
    finally:
        driver.quit()




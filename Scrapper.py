import sys
import time
import pyautogui
from rich import print
from rich.tree import Tree
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

url = 'https://www.netflix.com/in/title/81614454' if len(
    sys.argv) == 1 else sys.argv[1]

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get('https://www.netflix.com/in/title/81614454')

print("[green]Movie Name[/green] : {0}\n".format(driver.find_element(
    By.XPATH, '//*[@id="section-hero"]/div[1]/div[1]/div[2]/div/h1').text))
try:
    description = driver.find_element(
        By.XPATH, '//*[@id="section-hero"]/div[1]/div[1]/div[2]/div/div[2]/div[1]').text
    print(
        "[green]Description[/green] : {0}\n".format(
            driver.find_element(
                By.XPATH,
                '//*[@id="section-hero"]/div[1]/div[1]/div[2]/div/div[2]/div[1]').text))
    try:
        casts = driver.find_element(
            By.XPATH,
            '//*[@id="section-hero"]/div[1]/div[1]/div[2]/div/div[2]/div[2]/div/span[2]').text.split(',')
        tree = Tree("[green]Cast[/green]")
        for cast in casts:
            tree.add(cast)
        print(tree)
    except BaseException:
        print("Cast : No Cast Given")
except BaseException:
    print("Description : No Description and Cast Given")

trailerButton = driver.find_element(
    By.XPATH, '//*[@id="section-additional-videos"]/div[2]/ul/li/div/button')

trailerButton.click()
time.sleep(1)
videoBox = driver.find_element(
    By.XPATH, '//*[@id="react-aria-modal-dialog"]/div[2]')

time.sleep(2)
pyautogui.moveTo(
    videoBox.location['x'] + 100,
    videoBox.location['y'] + 200,
    duration=0.5)
time.sleep(0.5)
try:
    sec = (
        float(
            driver.find_element(
                By.XPATH,
                '//*[@id="react-aria-modal-dialog"]/div[2]/div/div/div[2]/div[3]/div/div[4]/div/div[1]/div/div[2]/time').text.replace(
                ':',
                '.')) * 60) + 5
    FullScreenButton = driver.find_element(
        By.XPATH,
        '//*[@id="react-aria-modal-dialog"]/div[2]/div/div/div[2]/div[3]/div/div[4]/div/div[2]/button[2]')
    FullScreenButton.click()
    time.sleep(sec)
except BaseException:
    driver.refresh()

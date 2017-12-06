#! /usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pymouse import PyMouse
import random
import time
import json
import multiprocessing

class GeetestCracker:
  def __init__(self, driver):
    self.driver = driver

  def MouseMoveSim(self, geetest_btn):
    self.driver.set_window_size(1280, 800)
    # self.driver.maximize_window()
    btn_loc = geetest_btn.location
    mouse = PyMouse()
    print(btn_loc)

    move_step = 30
    start_locx, start_locy = btn_loc['x'] - move_step*random.randint(8, 15), (btn_loc['y'] + 180);

    print("move to:%d, %d" % (start_locx, start_locy))
    mouse.move(start_locx, start_locy)
    for step in range(0, random.randint(17, 20)):
      time.sleep(.05 + random.uniform(0, .05))
      locx = start_locx + step * move_step + random.randint(0, 10)
      locy = start_locy + random.randint(-10, 10)
      print("move to:%d, %d" % (locx, locy))
      mouse.move(locx, locy)

    time.sleep(.05 + random.uniform(0, .1))
    mouse.click(locx, locy)
# '//*[@id="pro-operation"]/a'

def LoadCoockie(driver, fname):
  with open(fname) as cf:
    cookies = json.load(cf)
    for cookie in cookies:
      print(cookie)
      driver.add_cookie(cookie)

def GetCookie(ck_file):
  with open(ck_file, "w") as ck:
    cookie = driver.get_cookies()
    json.dump(cookie, ck)


if __name__ == "__main__":
  ck_file = "cookie.tmp"
  product_url = 'https://www.vmall.com/product/173840389.html'
  epoch = time.mktime(time.strptime("2017-12-08 10:08:00", "%Y-%m-%d %H:%M:%S"))
  print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(epoch)))
  buy_url = "https://sale.vmall.com/mate10pd.html?mainSku=81139976&backUrl=https%3A%2F%2Fwww.vmall.com%2Fproduct%2F173840389.html%2381139976&_t="
  buy_url += str(int(epoch*1000 + random.randint(2, 6)));
  print(buy_url)
  driver = webdriver.Chrome()
  driver.get(product_url)
  time.sleep(120)
  GetCookie(ck_file)
  LoadCoockie(driver, ck_file);
  driver.get(product_url)

  while (time.time() < epoch - 2):
    pass

  driver.get(buy_url)
  # GetCookie()
  # driver.find_element_by_xpath('//*[@id="pro-operation"]/a/span').click()
  # lgn_link = WebDriverWait(driver, 10, 0.01).until(
  #   EC.element_to_be_clickable((By.XPATH, '//*[@id="top-index-loginUrl"]')))
  # lgn_link.click()
  # geetest_btn = WebDriverWait(driver, 50, 0.01).until(EC.presence_of_element_located((By.XPATH, '//*[@id="captcha1"]/div[2]/div[2]/div[1]/div[3]')))
  # gtc = GeetestCracker(driver)
  # gtc.MouseMoveSim(geetest_btn)
  # user = driver.find_element_by_xpath('//*[@id="login_userName"]')
  # user.clear()
  # user.send_keys("15850740010")
  # passwd = driver.find_element_by_xpath('//*[@id="login_password"]')
  # passwd.clear()
  # passwd.send_keys('Hobot123.')
  # driver.find_element_by_xpath('//*[@id="btnLogin"]').click()
  # buy_btn = WebDriverWait(driver, 100, 0.001).until(
  #   EC.element_to_be_clickable((By.XPATH, '//*[@id="pro-operation"]/a')))
  # buy_btn.click()

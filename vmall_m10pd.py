#! /usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# from pymouse import PyMouse
import random
import time
import json
import multiprocessing

epoch = time.mktime(time.strptime("2017-12-13 10:08:00", "%Y-%m-%d %H:%M:%S"))

def LoadCookie(driver, fname):
  with open(fname) as cf:
    cookies = json.load(cf)
    for cookie in cookies:
      print(cookie)
      driver.add_cookie(cookie)

def GetCookie(ck_file):
  with open(ck_file, "w") as ck:
    cookie = driver.get_cookies()
    json.dump(cookie, ck)

def GoBuy(cookie_file, product_url):
  driver = webdriver.Chrome()
  buy_url = "https://sale.vmall.com/mate10pd.html?mainSku=81139976&backUrl=https%3A%2F%2Fwww.vmall.com%2Fproduct%2F173840389.html%2381139976&_t="
  buy_url += str(int(epoch*1000 + random.randint(0, 10)));
  print(buy_url)
  driver.get(product_url)
  driver.maximize_window()
  LoadCookie(driver, cookie_file)
  driver.get(product_url)

  while (time.time() * 1000 < epoch * 1000):
    print("now:%d, epoch:%d" % (time.time()*1000, epoch * 1000))
    time.sleep(.001)

  driver.get(buy_url)
  print("done")


if __name__ == "__main__":
  ck_file = "cookie.tmp"
  product_url = 'https://www.vmall.com/product/173840389.html'
  print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(epoch)))
  driver = webdriver.Chrome()
  driver.get(product_url)
  driver.maximize_window()
  WebDriverWait(driver, 500, 0.01).until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="pro-operation"]/a'), "即将开始"))
  # time.sleep(60)
  GetCookie(ck_file)

  record = []
  for i in range(1):
    proc = multiprocessing.Process(target = GoBuy, args = (ck_file, product_url))
    proc.start()
    record.append(proc)

  for p in record:
    p.join()


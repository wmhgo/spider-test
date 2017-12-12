#! /usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from selenium.common.exceptions import WebDriverException
import random
import time
import multiprocessing
import platform
import re
import sys

# epoch = time.mktime(time.strptime("2017-12-13 10:08:00", "%Y-%m-%d %H:%M:%S"))

def GoBuy(product_url, cookies, buy_time):
  dcap = dict(DesiredCapabilities.PHANTOMJS)

  ua = ""
  os_type = platform.system()
  if re.match("Linux", os_type):
    ua = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
  elif re.match("Windows", os_type):
    ua = ""

  # 设置useragent
  dcap["phantomjs.page.settings.userAgent"] = ua
  # 不载入图片，爬页面速度会快很多
  dcap["phantomjs.page.settings.loadImages"] = False
  # 设置代理
  # service_args = ['--proxy=127.0.0.1:9999', '--proxy-type=socks5']
  # 打开带配置信息的phantomJS浏览器
  driver = webdriver.PhantomJS(desired_capabilities=dcap)
  buy_url = "https://sale.vmall.com/mate10pd.html?mainSku=81139976&backUrl" \
            "=https%3A%2F%2Fwww.vmall.com%2Fproduct%2F173840389.html%2381139976&_t="
  buy_url += str(int(buy_time*1000 + random.randint(0, 10)))
  print(buy_url)
  driver.get(product_url)
  for ck in cookies:
    driver.add_cookie(ck)
  # driver.get(product_url)

  while (time.time() * 1000 < buy_time * 1000):
    print("now:%d, buy_time:%d" % (time.time()*1000, buy_time * 1000))
    time.sleep(.001)

  driver.get(buy_url)
  # driver.save_screenshot("prd.png")
  print("done")
  time.sleep(600)

def GetBuyTime():
  cur_tm = time.localtime()
  if (cur_tm.tm_wday != 0 and cur_tm.tm_wday != 2 and cur_tm.tm_wday != 4):
    print("今天是星期%d, 不开卖, 退出..." % (cur_tm.tm_wday + 1))
    sys.exit(-1)
  return time.mktime(time.strptime("%04d-%02d-%02d %02d:%02d:%02d" %
                                   (cur_tm.tm_year, cur_tm.tm_mon, cur_tm.tm_mday, 10, 8, 0),
                                   "%Y-%m-%d %H:%M:%S"))


if __name__ == "__main__":
  buy_time = GetBuyTime()
  print("本次抢购时间：%s" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(buy_time))))
  product_url = 'https://www.vmall.com/product/173840389.html'
  driver = webdriver.Chrome()
  driver.delete_all_cookies()
  driver.get(product_url)
  driver.maximize_window()
  WebDriverWait(driver, 500, 0.01).until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="pro-operation"]/a'),
                                         "即将开始"))

  record = []
  for i in range(1):
    proc = multiprocessing.Process(target = GoBuy, args = (product_url, driver.get_cookies(), buy_time))
    proc.start()
    record.append(proc)

  for p in record:
    p.join()


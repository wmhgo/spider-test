#! /usr/bin/env python
import time
import os
from selenium import webdriver

driver = webdriver.Chrome()

def restart_server():
  procs = os.popen('ps -ef | grep ./server | grep -v grep', "r").readlines()
  if not procs:
    os.system('cd /home/nj-gpu0/human_flow_analysis/build/bin')
    os.system('nohup ./server >/dev/null 2>/dev/null &')
    return True
  else:
    return False

def restart_web():
  driver.fullscreen_window()
  driver.get('')
  driver.get('')
  driver.find_element_by_xpath('').click()
  driver.find_element_by_xpath('').click()
  driver.find_element_by_xpath('').click()

if __name__ == "__main__":
  while True:
    if restart_server():
      restart_web()
    time.sleep(1)
#! /usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

class JDBuyer:
  def __init__(self, driver):
    self.driver = driver
    self.cookies = []

  def Login(self, login_url, username, passwd):
    self.driver.get(login_url)
    self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div/div[3]/a').click()
    name_edit = self.driver.find_element_by_xpath('//*[@id="loginname"]')
    name_edit.clear()
    name_edit.send_keys(username)
    passwd_edit = self.driver.find_element_by_xpath('//*[@id="nloginpwd"]')
    passwd_edit.clear()
    passwd_edit.send_keys(passwd)
    self.driver.find_element_by_xpath('//*[@id="loginsubmit"]').click()
    self.cookies = self.driver.get_cookies()

  def Reserve(self, reserve_url):
    reserve_btn = self.driver.find_element_by_xpath('//*[@id="btn-reservation"]')
    if (reserve_btn):
      reserve_btn.click()
    # buy_btn =
    time.sleep(20)

  def Buy(self, buy_url):
    self.driver.get(buy_url)

if __name__ == "__main__":
  jd_login_url = 'https://passport.jd.com/new/login.aspx'
  buyer = JDBuyer(webdriver.Chrome())
  buyer.Login(jd_login_url, "15850740010", "gj86818.")
  buyer.Reserve('https://item.jd.com/5716981.html?dist=jd')

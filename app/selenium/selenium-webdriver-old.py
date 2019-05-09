from selenium import webdriver
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest

class seleniumTest(unittest.TestCase):
	def setUp(self):
		while 1:
			try:
				self.driver= webdriver.Remote(command_executor='http://selenium-chrome:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)

				break
			except Exception as e:
				time.sleep(1)
				print(e)

	def test_functionality(self):
		driver = self.driver
		driver.get("http://localhost:8000/")
		self.assertIn("localhost", driver.title)
#		element = driver.find_element_by_xpath("/html/body/header/nav/div/div/ul/li[3]/a/span")#.click()
		element = driver.find_element_by_id('HPLogInButton')
		assert True

	def tearDown(self):
		self.driver.close()

if __name__ == "__main__":
	unittest.main()

# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import unittest, time, re

class Rrr(unittest.TestCase):
	def setUp(self):        
		capabilites = {"browserName": "chrome", "version": " "}
		while 1:
			try:
				self.driver= webdriver.Remote(command_executor="http://selenium-chrome:4444/wd/hub", desired_capabilities=DesiredCapabilities.CHROME)
				#self.driver.implicitly_wait(30)
				self.base_url = "https://localhost:8000/"
				self.verificationErrors = []
				self.accept_next_alert = True
				break
			except Exception as e:
				time.sleep(1)
				print(e)
	
	def test_login(self):
		driver = self.driver
		driver.get("http://localhost:8000/")
		driver.find_element_by_id("HPLogInButton").click()
		driver.find_element_by_id("id_username").click()
		driver.find_element_by_id("id_username").clear()
		driver.find_element_by_id("id_username").send_keys("x")
		driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Log in'])[1]/following::div[3]").click()
		driver.find_element_by_id("id_password").click()
		driver.find_element_by_id("id_password").clear()
		driver.find_element_by_id("id_password").send_keys("password")
		driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Log in'])[1]/following::button[1]").click()
		driver.find_element_by_name("query").click()
		driver.find_element_by_name("query").clear()
		driver.find_element_by_name("query").send_keys("steak")
		driver.find_element_by_name("query").send_keys(Keys.ENTER)
		driver.find_element_by_link_text("Learn more").click()
		driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Create Meal'])[1]/following::span[1]").click()
	
	def is_element_present(self, how, what):
		try: self.driver.find_element(by=how, value=what)
		except NoSuchElementException as e: return False
		return True
	
	def is_alert_present(self):
		try: self.driver.switch_to_alert()
		except NoAlertPresentException as e: return False
		return True
	
	def close_alert_and_get_its_text(self):
		try:
			alert = self.driver.switch_to_alert()
			alert_text = alert.text
			if self.accept_next_alert:
				alert.accept()
			else:
				alert.dismiss()
			return alert_text
		finally: self.accept_next_alert = True
	
	def tearDown(self):
		# To know more about the difference between verify and assert,
		# visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
		self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
	unittest.main()

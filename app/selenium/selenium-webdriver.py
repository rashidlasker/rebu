from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import unittest, time, re

class Rrr(unittest.TestCase):
	def setUp(self): 
		while 1:
			try:
				self.driver= webdriver.Remote(command_executor="http://selenium-chrome:4444/wd/hub", desired_capabilities=DesiredCapabilities.CHROME)
				self.verificationErrors = []
				break
			except Exception as e:
				time.sleep(1)
				print(e)
	
	def test_login(self):
		driver = self.driver
		time.sleep(5)
		driver.get("http://web:8000/")
		assert "Rebu" in driver.title
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
	
	def tearDown(self):
		# To know more about the difference between verify and assert,
		# visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
		self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
	unittest.main()

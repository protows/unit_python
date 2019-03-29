# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=r'N:\xampp\htdocs\python\geckodriver.exe')

    def test_search_in_python_org(self):
    	driver = self.driver
    	driver.get("http://www.mail.ru")
    	elem = driver.find_element_by_id("g")
    	elem.clear()
    	elem.send_keys("fghfgh/f65h46fhw33454$#")
    	elem.send_keys(Keys.RETURN)
    	print('ok first')
    	assert "По данному запросу ничего не найдено" not in driver.page_source
    	print('ok second')

    def tearDown(self):
    	self.driver.close()

if __name__ == "__main__":
	unittest.main()












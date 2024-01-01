import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestPythonWebsite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.pypi.org/")

    def test_search_in_python_org(self):
        driver = self.driver
        self.assertIn("PyPI", driver.title)
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("selenium")
        search_box.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()

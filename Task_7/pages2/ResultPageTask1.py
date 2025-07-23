from selenium.webdriver.common.by import By

class ResultPage:

    def __init__(self, browser):
        self._driver = browser

    def color_zip(self):
        color_zip = self._driver.find_element(By.CSS_SELECTOR, "#zip-code").value_of_css_property("color")
        return color_zip
    
    def color_firstName(self):
        color_firstName = self._driver.find_element(By.CSS_SELECTOR, "#first-name").value_of_css_property("color")
        return color_firstName
    
    def color_lastName(self):
        color_lastName = self._driver.find_element(By.CSS_SELECTOR, "#last-name").value_of_css_property("color")
        return color_lastName
    
    def color_address(self):
        color_address = self._driver.find_element(By.CSS_SELECTOR, "#address").value_of_css_property("color")
        return color_address
    
    def color_city(self):
        color_city = self._driver.find_element(By.CSS_SELECTOR, "#city").value_of_css_property("color")
        return color_city
    
    def color_country(self):
        color_country = self._driver.find_element(By.CSS_SELECTOR, "#country").value_of_css_property("color")
        return color_country
    
    def color_mail(self):
        color_mail = self._driver.find_element(By.CSS_SELECTOR, "#e-mail").value_of_css_property("color")
        return color_mail
    
    def color_phone(self):
        color_phone = self._driver.find_element(By.CSS_SELECTOR, "#phone").value_of_css_property("color")
        return color_phone
        
    def color_job(self):
        color_job = self._driver.find_element(By.CSS_SELECTOR, "#job-position").value_of_css_property("color")
        return color_job
    
    def color_company(self):
        color_company = self._driver.find_element(By.CSS_SELECTOR, "#company").value_of_css_property("color")
        return color_company
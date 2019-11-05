import argparse, sys
import unittest
from selenium import webdriver
from setup import BaseClassForTesting
import time
# try:
#     address = sys.argv[1]
# except IndexError:
#     address = 'http://127.0.0.1:8000'



class SignupForm(BaseClassForTesting):

    def test_signup_form_protected_by_captcha(self):
        driver = self.driver
        driver.get(self.address + '/account/signup')
        username_input = driver.find_element_by_name('username')
        #fill_user_name
        username_input.send_keys('automatedtestuser')
        email_input = driver.find_element_by_name('email')
        #fill email
        email_input.send_keys('me@example.com')
        password_1_input = driver.find_element_by_name('password1')
        #fill password
        password_1_input.send_keys('passwordexample')
        password_2_input = driver.find_element_by_name('password2')
        #fill password
        password_2_input.send_keys('passwordexample')
        signup_button = driver.find_element_by_class_name('btn-submit2')
        #send form
        signup_button.click()
        time.sleep(1)
        assert 'Please successfully complete the captcha' in driver.page_source


if __name__ == "__main__":
    unittest.main()
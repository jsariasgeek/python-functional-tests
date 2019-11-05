import time
import unittest
from setup import BaseClassForTesting

class TestQuestionsView(BaseClassForTesting):
    def test_table_questions_is_rendering(self):
        self.driver.get(self.address + '/questions/')
        time.sleep(1)
        table_title = self.driver.find_element_by_class_name('table_title')
        assert 'Questions and Answers' in table_title.text

        #check table is rendering
        questions = self.driver.find_element_by_xpath("//div[@id='Newest']/div[@class='row-fluid']")
        container = self.driver.find_element_by_id('Newest')
        assert container.text


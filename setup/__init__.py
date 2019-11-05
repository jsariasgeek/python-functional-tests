import sys, getopt
import argparse
import unittest
from selenium import webdriver

args = sys.argv
parser = argparse.ArgumentParser()
parser.add_argument('--address', help='address where project is running')
args = parser.parse_args()

try:
    address = args.address
except IndexError:
    address = None

address = address if address else 'http:127.0.0.1:8000'

class BaseClassForTesting(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.address = address

    def tearDown(self) -> None:
        self.driver.close()
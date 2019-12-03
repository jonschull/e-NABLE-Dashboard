from collections import OrderedDict
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from arrow import now
def date():return now('America/New_York').format('YYYY-MM-DD')
def time():return now('America/New_York').format('HH:mm')

import pandas as pd
from pandas import DataFrame

def Driver(HEADLESS=False):
    if HEADLESS:
        #https://stackabuse.com/getting-started-with-selenium-and-python/
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(options=options)
        driver.set_window_size(1440, 900)
    else:
        driver=webdriver.Chrome()        
    return driver
    

import json
import requests
import urllib.request
import pandas as pd
import os.path
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By


myencoding = 'utf-8'
myparser = 'html.parser'
myurl = 'https://flixpatrol.com/'
filepath = '/allnew/python/mini_project/chromedriver'

# @app.get('/')
# def selenium_test():
driver = webdriver.Chrome(filepath)
driver.get(myurl)
time.sleep(3)
driver.quit()
# html = urllib.request.urlopen('https://flixpatrol.com/title/vincenzo-2021/top10/australia/')
# print(html)
# soup = BeautifulSoup(html , 'html.parser')
# result = soup.find('tbody')
# print(result)
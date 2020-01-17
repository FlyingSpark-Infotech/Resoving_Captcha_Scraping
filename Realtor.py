from selenium import webdriver
from bs4 import BeautifulSoup
import requests, random, string
import csv, sys, time
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from tbselenium.tbdriver import TorBrowserDriver
from tbselenium import tbdriver
import pandas as pd
import openpyxl
import xlsxwriter
import subprocess, os, platform
import psutil
import re
from selenium import webdriver
from lxml import etree
import sys
import os
import re
import random
import time
from selenium.webdriver.common.proxy import ProxyType
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
class Realtor():
    def __init__(self):
        # need to set chrome path here.
        #self.driver = webdriver.Chrome()
        user_agent_list=0
        with open('user_agent.txt', 'rb') as f:
            for line in f:
                text=line.decode(errors='ignore')
                user_agent_list = text.split('\n')
            
        webdriver.DesiredCapabilities.PHANTOMJS['phantomjs.page.customHeaders.{}'.format('User-Agent')] = random.choice(user_agent_list)
        self.browser = webdriver.PhantomJS()
        # proxy = webdriver.Proxy()
        # proxy.proxy_type = ProxyType.MANUAL
        # proxy.http_proxy = '127.0.0.1:56923'
        # proxy.add_to_capabilities( webdriver.DesiredCapabilities.PHANTOMJS)
        self.browser.start_session(webdriver.DesiredCapabilities.PHANTOMJS)
        self.browser.implicitly_wait(120)
        self.browser.set_page_load_timeout(120)
        self.browser.get("https://www.realtor.com/realestateandhomes-detail/25312-Germaine-Ln_Hemet_CA_92544_M16085-80269")
        #self.driver.get('https://www.realtor.com/realestateandhomes-detail/25312-Germaine-Ln_Hemet_CA_92544_M16085-80269')
        # self.driver = webdriver.Firefox(firefox_profile=profile, firefox_binary=binary)
        # self.driver = webdriver.Chrome(executable_path='../utility/chromedriver.exe', chrome_options=chrome_options)

    # method to get items from given link.
    def getItems(self):
        df=pd.read_excel("/xxx/xxxxx/delhi/sample1.xlsx")
        a=df['Site Address']
        b=df['Site City']
        c=df['Site State']
        d=df['Site Zip']
        items = []
        #keywords = ['512 W 10th St Perris CA 92570', 'New York, NY', 'San Francisco, CA', 'Washington, CA']
        for keyword in (pd.concat([a,b,c,d],axis=1)).values.tolist():
        #keywords = ['25312 Germaine Ln	Hemet	Ca	92544','25445 Jerry Ln	Hemet	Ca	92544','1761 San Andres Dr	Hemet	Ca	92545'] 
        #for keyword in keywords:
            #print(keyword)
            self.browser.get('https://www.realtor.com/realestateandhomes-detail/25312-Germaine-Ln_Hemet_CA_92544_M16085-80269')
            #search_box = self.driver.find_element_by_id("rdc-main-search-nav-hero-input")
            search_box = self.browser.find_element_by_id("searchBox")
            search_box.clear()
            search_box.send_keys(str(keyword))
            #search_btn = self.driver.find_element_by_xpath("//button[@class='rdc-btn_2q8dK rdc-btn-brand_28UWP search-btn']")
#             search_btn = self.browser.find_element_by_xpath("/html/body/div[5]/div[2]/section/div/div[1]/div[2]/div[1]/span/button[2]")
#             if search_btn:
            search_box.send_keys(Keys.ENTER)
            time.sleep(10)
            items.append((re.search('[$]+[0-9]+[,]+[0-9]+',self.getItemDetail()).group(0)))
            # break
        self.driver.close()
        return items


    def getItemDetail(self):
        data = []
        try:
            soup = BeautifulSoup(self.driver.page_source, u'html.parser')
            #image = soup.find("div", attrs={"class": "Tiles__TileBackground-fk0fs3-0 cSObNX"}).find("img")["src"]
            #price = soup.find("span").text
            price=soup.find(itemprop="price").getText()
            print(price)
#             for i in soup.find_all("div",class_="col-qv-xs-12 col-qv-sm-7 col-qv-md-12 col-qv-lg-7 qv-price-wrapper"):
#                 print(j.getText())
            # container = soup.find("div", attrs={"class": "resultsColumn"}).find("ul")
            # items = container.findAll("li", recursive=False)

        except:
            pass
        return price
    # method to start process.
    def start(self):
        items = self.getItems()
        print(items)
        df=pd.read_excel("/home/xxxx/xxxx/sample1.xlsx")
        print(df)
        df[' Realtor ']=items
        with pd.ExcelWriter('/home/xxxx/xxxxx/sample1.xlsx', engine='openpyxl',mode='a') as writer:
            df.to_excel(writer)
        #print("Items : ",items)
# main function call
if __name__ == "__main__":
    #objTH is an TruliaHelper class.
    objTH = Realtor()
    objTH.start()

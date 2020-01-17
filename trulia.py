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
for proc in psutil.process_iter():
    try:
        pinfo = proc.as_dict()
        # print(pinfo)
        pid = pinfo['ppid']
        if pinfo['exe'] :
            if "Tor Browser" in pinfo['exe']:
                os.system("taskkill /im firefox.exe /f")
    except psutil.NoSuchProcess:
        pass
    # print("#"*100)
# sys.exit(1)

filepath = "/home/xxxxx/xxxxx/tor-browser-linux64-8.0.8_en-US/tor-browser_en-US/Browser"
if platform.system() == 'Darwin':       # macOS
    subprocess.call(('open', filepath))
elif platform.system() == 'Windows':    # Windows
    os.startfile(filepath)
else:                                   # linux variants
    subprocess.call(('xdg-open', filepath))

class TruliaHelper():

    def __init__(self):
        self.url = 'https://www.trulia.com'
        # need to set chrome path here.
        tbpath = "/home/XX/XXXX/tor-browser-linux64-8.0.8_en-US/tor-browser_en-US"
        self.driver = TorBrowserDriver(tbb_path=tbpath, tbb_logfile_path='test.log')
        # self.driver = webdriver.Firefox(firefox_profile=profile, firefox_binary=binary)
        # self.driver = webdriver.Chrome(executable_path='../utility/chromedriver.exe', chrome_options=chrome_options)

    # method to get items from given link.
    def getItems(self):
        df=pd.read_excel("/home/XXXXX/XXXXX/XXXXXX.xlsx")
        a=df['Site Address']
        b=df['Site City']
        c=df['Site State']
        d=df['Site Zip']
        items = []
        # keywords = ['512 W 10th St Perris CA 92570', 'New York, NY', 'San Francisco, CA', 'Washington, CA']
        for keyword in (pd.concat([a,b,c,d],axis=1)).values.tolist():
#         keywords = ['512 W 10th St Perris CA 92570'] * 10
#         for keyword in keywords:
            self.driver.get(self.url)
            search_box = self.driver.find_element_by_id("homepageSearchBoxTextInput")
            search_box.clear()
            search_box.send_keys(str(keyword))
            search_btn = self.driver.find_element_by_xpath("//button[@data-auto-test-id='searchButton']")
            if search_btn:
                search_btn.click()
                time.sleep(10)
                items.append(self.getItemDetail())
            # break
        self.driver.close()
        return items


    def getItemDetail(self):
        data = {}
        try:
            soup = BeautifulSoup(self.driver.page_source, u'html.parser')
            #image = soup.find("div", attrs={"class": "Tiles__TileBackground-fk0fs3-0 cSObNX"}).find("img")["src"]
            price = soup.find("div", attrs={"class": "Text__TextBase-sc-1cait9d-0-div Text__TextContainerBase-sc-1cait9d-1 hlvKRM"}).text
            # container = soup.find("div", attrs={"class": "resultsColumn"}).find("ul")
            # items = container.findAll("li", recursive=False)
            print(price)
        except:
            pass
        return data
  
    # method to start process.
    def start(self):
        items = self.getItems()
        print("Items : ",items)
# main function call
if __name__ == "__main__":

    # objTH is an TruliaHelper class.
    objTH = TruliaHelper()
    objTH.start()

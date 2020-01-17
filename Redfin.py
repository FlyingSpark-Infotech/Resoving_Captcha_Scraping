from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from bs4 import BeautifulSoup
    from tbselenium.tbdriver import TorBrowserDriver
    import random, sys, time
    from fake_useragent import UserAgent
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
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    ua = UserAgent(cache=False)
    user_agent = ua.random
    class RedFinHelper():
            price=0
            def __init__(self):
                #self.price=0
                options = webdriver.ChromeOptions()
                options.add_argument("--incognito")
                self.options = webdriver.ChromeOptions()
                #chrome_options.add_argument('--proxy-server=%s' % PROXY)
                #self.chrome_options.add_argument("--incognito")
                #self.options = Options()
    #             self.options.add_argument("--incognito")
                options.add_argument("window-size=1400,600")
                options.add_argument('user-agent='+str(user_agent))

                self.driver = webdriver.Chrome(chrome_options=options)
                self.driver.get('https://www.redfin.com/CA/Hemet/25445-Jerry-Ln-92544/home/5744886')
                # self.driver = webdriver.Firefox(firefox_profile=profile, firefox_binary=binary)
                # self.driver = webdriver.Chrome(executable_path='../utility/chromedriver.exe', chrome_options=chrome_options)

            # method to get items from given link.
            def getItems(self):
                df=pd.read_excel("/xxxx/xxxxx/xxxxx/xxxxxx.xlsx")
                a=df['Site Address']
                b=df['Site City']
                c=df['Site State']
                d=df['Site Zip']
                items = []
                count=0
                #keywords = ['1744 Hoop Way Hemet Ca 92545','1744 Hoop Way Hemet Ca 92545']
                for keyword in (pd.concat([a,b,c,d],axis=1)).values.tolist():
                    count=count+1
                    print(count)
                    #print(' '.join(map(str,keyword)))
        #         keywords = ['512 W 10th St Perris CA 92570'] * 10
                #for keyword in keywords:
                    self.driver.get('https://www.redfin.com/CA/Hemet/25445-Jerry-Ln-92544/home/5744886')
                    #search_box = self.driver.find_element_by_id("search-box-input")
                    search_box = WebDriverWait(self.driver, 20).until(lambda driver: self.driver.find_element_by_xpath("//*[@id='search-box-input']"))
                    time.sleep(5)
                    actions = ActionChains(self.driver)
                    print(search_box)
                    actions.move_to_element(search_box.send_keys(str(' '.join(map(str,keyword)))))

                    #self.driver.implicitly_wait(10)
                    #search_box.send_keys(str(keyword))
                    #search_box.send_keys(str(' '.join(map(str,keyword))))
                    #time.sleep(5)
                    #actions.move_to_element(search_box).send_keys(Keys.ENTER).perform()
                    search_box.send_keys(Keys.ENTER)
                    time.sleep(5)
                    #time.sleep(5)
                    #search_box.clear()
    #                 search_btn = self.driver.find_element_by_xpath("//*[@id='headerUnifiedSearch']/div/form/div[1]/button")
    #                 if search_btn:
    #                     actions.move_to_element(search_btn).click().perform()
    #                     #search_btn.click()
    #                     time.sleep(10)
                    items.append(self.getItemDetail())
                    #items.append(re.search('[$]+[0-9]+[,]+[0-9]+',self.getItemDetail()).group(0))
                    # break
                #self.driver.back()
                self.driver.close()
                return items


            def getItemDetail(self):
                data = []
                try:
                    #df=pd.read_excel("/home/manoj/Documents/HADOOP/hadoop_project/delhi project/sample1.xlsx")
                    soup = BeautifulSoup(self.driver.page_source, u'html.parser')
                    #image = soup.find("div", attrs={"class": "Tiles__TileBackground-fk0fs3-0 cSObNX"}).find("img")["src"]
    #                 if (soup.find("div", attrs={"class": "Text__TextBase-sc-1cait9d-0-div Text__TextContainerBase-sc-1cait9d-1 hlvKRM"}))!=None:
    #                     self.price = soup.find("div", attrs={"class": "Text__TextBase-sc-1cait9d-0-div Text__TextContainerBase-sc-1cait9d-1 hlvKRM"}).text
    #                 else:
    #                     self.price=soup.find("span",attrs={"class":"h3"}).text
                    # container = soup.find("div", attrs={"class": "resultsColumn"}).find("ul")
                    self.price=soup.find("div",attrs={"class":"statsValue"}).text
                    print(self.price)


                    #                 for i in soup.find_all("div",attrs={"class":"statsValue"}):
    #                     if i.findAll("span")!=None:
    #                         p=i.findAll("span")
    #                         print(p[0].getText()+p[1].getText())
    #                         self.price=p[0].getText()+p[1].getText()

                    #price=soup.find("div",attrs={"class":"statsValue"}).text
                    # items = container.findAll("li", recursive=False)
                    #print(self.price)

                except:
                    pass
                if self.price!=0:
                    return self.price

            # method to start process.
            def start(self):
                import pandas
                items = self.getItems()
                print(items)
                df=pd.read_excel("/home/xxxxx/xxxxx/xxxxx.xlsx")
                df[' Redfin ']=items
                with pandas.ExcelWriter('/home/xxxxxx/xxxxx/xxxxx.xlsx', engine='openpyxl',mode='a') as writer:
                    df.to_excel(writer)
                #print("Items : ",items)
        # main function call
    if __name__ == "__main__":
            #objTH is an TruliaHelper class.
        objTH = RedFinHelper()
        objTH.start()

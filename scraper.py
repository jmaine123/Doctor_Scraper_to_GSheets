from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from lxml import etree, html
import time
import requests
import re
import pandas as pd
import requests
import json
import time
from selenium.webdriver.common.by import By
from dataclasses import dataclass, asdict
from gspread_dataframe import set_with_dataframe
import gspread as gs
from tqdm import tqdm
from threading import Thread



@dataclass
class DoctorDetails:
    name: str
    specialty: str
    age: int
    location: str



def get_doc_link(url):
    driver = webdriver.Chrome()
    driver.get(url)
    # driver.refresh()
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    s = soup.prettify()
    # print(s)
    dom = etree.HTML(str(soup))
    doc_links = dom.xpath('//a[contains(@class, "-ProviderLink")]/@href')
    
    for link in doc_links:
        get_doc_info(link)
    driver.close()
    
def get_doc_info(link):
    driver = webdriver.Chrome()
    full_link = f'https://doctors.sclhealth.org{link}'
    driver.get(full_link)
    # driver.refresh()
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    s = soup.prettify()
    # print(s)
    dom = etree.HTML(str(soup))
    name = dom.xpath('//h2[@id="provider-name"]/text()')
    print(name)
    
    
        
        

def main():
    get_doc_link('https://doctors.sclhealth.org/search?sort=networks%2Crelevance%2Cavailability_density_best&page=1')


if __name__ == "__main__":
    main()
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 10:12:40 2019

@author: james
"""

import bs4
import requests
from datetime import date
import os

today = str(date.today())

f=open("data/SUPERB/"+today+"SUPERB.csv","w", encoding='utf-8')
headers="Date_recorded,Picture_url,Title,Year,Type,Mileage,Engine Size,BHP,Transmition,Fuel Type,Price \n"
f.write(headers)

def clean(x):
    x.text.strip().replace(",","")
    

#The link that we are scraping data from
Glink = "https://www.autotrader.co.uk/car-search?sort=datedesc&postcode=CT14%209NQ&radius=1500&make=SKODA&model=SUPERB&include-delivery-option=on&year-from=2016&year-to=2018&fuel-type=Petrol&body-type=Estate&minimum-badge-engine-size=1.4&maximum-badge-engine-size=1.4&page="

for page in range(2,1000):
    #requests gets the data from the link
    data = requests.get(Glink+str(page))
    soup = bs4.BeautifulSoup(data.content, 'html.parser')
    print("Page Numer: " + str(page))
    
    
    articles=soup.find_all("article")
    if len(articles)==0:
        print("no pages")
        break
    else:
        for item in articles:
            
            data=[]
            data.append(today)
            data.append(str(item.a.img).split("src=")[1][:-3][1:])
            sections=item.find_all("section")
            data.append(sections[0].h2.text.strip().replace(",",""))
            
            sec=sections[0].find_all("li")
            for item in sec[:7]:
                if item!="":
                    data.append(item.text.strip().replace(",",""))
            
            
            data.append(sections[1].a.div.text.strip().replace(",","")[1:])
            
            #if data[]
            
            f.write(str(data)[:-1][1:].replace("'","")+"\n")
        
f.close()

path="data/SUPERB/"
          
CSVs = []
for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(".csv"):
            CSVs.append(os.path.join(root, file))

with open('SUPERB_data.csv', 'w', encoding='utf-8') as singleFile:
    filenumber=0
    for csvFile in CSVs:
        index=0
        for line in open(csvFile, 'r'):
            if index!=0 or filenumber==0:    
                singleFile.write(line)
            index+=1
        filenumber+=1 
singleFile.close()
    
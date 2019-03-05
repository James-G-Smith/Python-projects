# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 10:12:40 2019

@author: james
"""

import bs4
import requests
from datetime import date
from glob import glob
import os


today = str(date.today())

f=open("data/CUPRA/"+today+"cupra.csv","w", encoding='utf-8')
headers="Date_recorded,Picture_url,Title,Year,Type,Mileage,Engine Size,BHP,Transmition,Fuel Type,Price \n"
f.write(headers)

def clean(x):
    x.text.strip().replace(",","")
    

#The link that we are scraping data from
link="https://www.autotrader.co.uk/car-search?sort=sponsored&radius=1500&postcode=ct149nq&onesearchad=Used&onesearchad=Nearly%20New&onesearchad=New&make=SEAT&model=LEON&page="
Glink = "https://www.autotrader.co.uk/car-search?sort=sponsored&radius=1500&postcode=ct149nq&onesearchad=Used&onesearchad=Nearly%20New&onesearchad=New&make=VOLKSWAGEN&model=GOLF&keywords=GTI&page="
Clink = "https://www.autotrader.co.uk/car-search?sort=sponsored&radius=1500&postcode=ct149nq&onesearchad=Used&onesearchad=Nearly%20New&onesearchad=New&make=SEAT&model=LEON&quantity-of-doors=5&keywords=cupra&page="

for page in range(1,1000):
    #requests gets the data from the link
    data = requests.get(Clink+str(page))
    soup = bs4.BeautifulSoup(data.content, 'html.parser')
    print("Page Numer: " + str(page))
    
    
    articles=soup.find_all("article")
    if len(articles)==0:
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
            
            f.write(str(data)[:-1][1:].replace("'","")+"\n")
        
f.close()

path="data/CUPRA/"
          
CSVs = []
for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(".csv"):
            CSVs.append(os.path.join(root, file))

with open('cupra_data.csv', 'w') as singleFile:
    filenumber=0
    for csvFile in CSVs:
        index=0
        for line in open(csvFile, 'r'):
            if index!=0 or filenumber==0:    
                singleFile.write(line)
            index+=1
        filenumber+=1 
singleFile.close()
   

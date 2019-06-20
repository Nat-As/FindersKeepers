#!/usr/bin/python3

'''
National Lab Research Bot
James Andrews <jandews7348@floridapoly.edu>
Scout 11 of 17 national LAB databases for topics of interest
'''

import http.client
import requests
import json
import sys
import matplotlib.pyplot as plt
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.item import Item, Field

try:
    query = sys.argv[1]
except:
    print("Error! No query specefied!")
    exit()

ames = "https://www.ameslab.gov/"#https://www.ameslab.gov/search/site/rats
argonne = "https://www.anl.gov/"#https://www.anl.gov/search-public#q=rats&sort=relevancy&site=Argonne%20National%2BLaboratory
brookhaven = "https://www.bnl.gov/world/"#https://www.bnl.gov/search/results.php#10000|rats|29
fermilab = "http://www.fnal.gov/"#https://library.fnal.gov/search/rats
berkely = "https://www.lbl.gov/"#https://search.lbl.gov/?q=rats&search_type=google#gsc.tab=0&gsc.q=rats&gsc.page=1
oakridge = "https://www.ornl.gov/"#https://www.ornl.gov/search-results#stq=rats&stp=1
pacificnw = "https://www.pnnl.gov/"
princeton = "https://www.pppl.gov/"
slac = "https://www6.slac.stanford.edu/"
jlab = "https://www.jlab.org/"
losalamos = "https://www.lanl.gov/"

def outreach():
    print("Connecting to Ames...")
    a = requests.get(ames)
    if a.status_code == 200: print(" └──╼ Success!")
    else: 
        print(" └╼ Failed!")
        print(a.status_code)
        
    print("Connecting to Argonne...")
    b = requests.get(argonne)
    if b.status_code == 200: print(" └──╼ Success!")
    else: 
        print(" └╼ Failed!")
        print(b.status_code)

    print("Connecting to Brookhaven...")
    c = requests.get(brookhaven)
    if c.status_code == 200: print(" └──╼ Success!")
    else: 
        print(" └╼ Failed!")
        print(c.status_code)

    print("Connecting to Fermilab...")
    d = requests.get(fermilab)
    if d.status_code == 200: print(" └──╼ Success!")
    else: 
        print(" └╼ Failed!")
        print(d.status_code)

    print("Connecting to Berkely...")
    e = requests.get(berkely)
    if e.status_code == 200: print(" └──╼ Success!")
    else: 
        print(" └╼ Failed!")
        print(e.status_code)

    print("Connecting to Oakridge...")
    f = requests.get(oakridge)
    if f.status_code == 200: print(" └──╼ Success!")
    else: 
        print(" └╼ Failed!")
        print(f.status_code)

    print("Connecting to Pacific Northwest...")
    g = requests.get(pacificnw)
    if g.status_code == 200: print(" └──╼ Success!")
    else: 
        print(" └╼ Failed!")
        print(g.status_code)

    print("Connecting to Princeton...")
    h = requests.get(princeton)
    if h.status_code == 200: print(" └──╼ Success!")
    else: 
        print(" └╼ Failed!")
        print(h.status_code)

    print("Connecting to Slac...")
    i = requests.get(slac)
    if i.status_code == 200: print(" └──╼ Success!")
    else: 
        print(" └╼ Failed!")
        print(i.status_code)

    print("Connecting to Jlab...")
    j = requests.get(jlab)
    if j.status_code == 200: print(" └──╼ Success!")
    else: 
        print(" └╼ Failed!")
        print(j.status_code)

    print("Connecting to Los Alamos...")
    k = requests.get(losalamos)
    if k.status_code == 200: print(" └──╼ Success!")
    else: 
        print(" └╼ Failed!")
        print(k.status_code)

outreach()#Find 11 DB's

class amesfield(Item):
    url= Field()

class amesspider(CrawlSpider):
    alpha = (ames + "search/site/" + query)
    name = 'crawltest'
    allowed_domains = [ames]
    start_urls = [alpha]
    rules = (Rule(LxmlLinkExtractor(allow=()), callback='parse_obj', follow=True),)

    def parse_obj(self,response):
        Item = amesfield()
        Item['url'] = []
        for link in LxmlLinkExtractor(allow=(),deny = self.allowed_domains).extract_links(response):
            Item['url'].append(link.url)
        return Item
amesspider.parse_obj()

def spider():
    print("")
    print("Searching for references to ", query)
    
    alpha = (ames + "search/site/" + query)
    print("    •", alpha)
    aq = requests.get(alpha)
    
    with open('ames-data.txt', 'w') as file:
        file.write(aq.text)

#spider()#Release the spider

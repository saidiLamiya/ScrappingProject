
from django.core.management.base import BaseCommand
import scrapy 
from scrapy.linkextractors import LinkExtractor
from scrapy import Selector
import re
import pandas as pd
from scrapy.crawler import CrawlerProcess
from api.models import Keyword, User
from urllib.parse import urlparse
from api.models import User, Event, School
import random
import time

class Command(BaseCommand):
    help='hello'

    def handle(self,*args,**options):
        '''
        This is the function's decription
        '''
        print('hello again test')
        
        process = CrawlerProcess()
        process.crawl(firstSpider)
        process.start()
  

class firstSpider(scrapy.Spider): 
    name = "basic"
    Schools=""
    start_urls = []
    custom_settings = {
            'DOWNLOAD_DELAY': 0,
            'CONCURRENT_REQUESTS_PER_DOMAIN': 1
        }
    def __init__(self):
        
            for ker in School.objects.all():
                for key in Keyword.objects.all():
                    url = 'https://www.google.com/search?q=site:http://ma.linkedin.com/in/+%22gmail%22+%22'
                    #print("TEEEEEEEEEST",str(ker).replace(" ","+"), str(key).replace(" ","+"))
                    url=url+str(ker).replace(" ","+")+'%22+%22'+str(key).replace(" ","+")
                    url=url+"%22&start="
                    print(url)

                    for start in range(0, 100, 10):
                            self.start_urls.append(url + str(start))
    
    def parse(self, response):
        #print('response url:', response.url)
        df = pd.DataFrame()
        xlink = LinkExtractor()

        schoools=[]
        for ber in School.objects.all():
            schoools.append(str(ber))
        print("OUR SCHOOLS",schoools)

        link_list=[]
        link_text=[]
        divs = response.xpath('//div')
        text_list=[]    
        text_list1=[]   
        text_list2=[]   
        text_list3=[]   #nom
        text_list5=[]   #emails  
        text_list6=[]   #linkedin
        text_list7=[]   #prenom
        text_list8=[]   #school

        for span in divs.xpath('text()'):
            if len(str(span.get()))>100:

                text_list.append(span.get().lower()) 

                def func(s, pat):
                    pat = r'\b\S*%s\S*\b' % re.escape(pat) 
                    return re.findall(pat, s)
                def listToString(s): 
                    str1 = ""
                    return (str1.join(s))
            
                for i in text_list:
                    a=func(i,"@")
                    for j in schoools:
                        if( j in i):
                            res=j
                print(a)
                text_list1.append(a)

                for b in text_list1:
                    k=listToString(b) 
                print(k)  
                text_list2.append(k)
                    
            #print('LIST OF EMAILS   ',menu)


        for link in xlink.extract_links(response):
            if  'linkedin' in link.text:
                l=str(link)
                l1=l[39:150]

                l5=(link.text).split('-')[0]
                prenom1=l5.split(' ')[0]
                prenom=prenom1.lower()
                nom1=l5.replace(prenom1,"")
                nom=(" ".join(nom1.split())).lower()
                print(prenom)
                print(prenom,nom)
                linkdin=l1.split('&')[0]
                print(linkdin)
                l1.split('&')
         
                for i in text_list2:

                    if(prenom in i) or (nom in i):
                        zebra=i
                        zbr=listToString(i)
                            
                        if len(zebra):
                                    text_list5.append(zbr)

                                    text_list7.append(prenom)
                                    text_list3.append(nom)
                                    text_list6.append(linkdin)
                                    text_list8.append(res)
                                    if((text_list6.count(linkdin))>1 or (text_list5.count(zbr))>1):
                                        text_list5.pop()
                                        text_list8.pop()
                                        text_list7.pop()
                                        text_list3.pop()
                                        text_list6.pop()
      
                link_text.append(link.text)

        df['nom']=text_list3
        df['prenom']=text_list7
        df['email'] = text_list5
        df['school']=text_list8
        df['linkedin']=text_list6

        df.to_csv('output11.csv', mode='a',header=False,index=False)
        time.sleep(random.randint(20,30))
    
        #df = pd.read_csv(r'output11.csv')
        #df[~df.duplicated(subset=['textmeta'])].to_csv('output(clean1).csv',index=False)

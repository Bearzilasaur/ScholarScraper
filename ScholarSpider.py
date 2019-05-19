'''
---------------------------------------------------------------------
Takes a dict as input (?or two tuples) and scrapes google scholar for 
each key:value pair. Intended use: pass an Embayment name as key and 
keywords as values. Output in numpy format. 
=====================================================================
Author: Mitchell Baum
=====================================================================
'''
import requests
from bs4 import BeautifulSoup
import numpy
import time
import random
import re


'''Article class for storing scraped information. Contains as_list 
method which returns the information as a list and as_dict which 
returns a dict'''

class article:
    def __init__(self, no, embayment, bsObj):
        
        
        self.no         = no
        self.embayment  = embayment
        self.title      = bsObj.find('h3', {'class':'gs_rt'}).text
        self.auth, self.dateyear= bsObj.find('div', {'class':'gs_a'}).text.split('-')[0:2]
        self.abstract   = bsObj.find('div', {'class':'gs_rs'}).text
        self.citations  = bsObj.find('div', {'class': 'gs_fl'}).find(text=re.compile("^Cited by"))
        self.link       = bsObj.find('h3', {'class':'gs_rt'}).find('a', href = True)['href']
    
    '''Method which returns the information as a list with all the information stored in the class'''
    def as_array(self):
        x = numpy.array([[
            self.no,
            self.embayment,
            self.title,
            self.auth,
            self.abstract,
            self.dateyear,
            self.link
        ]])
        return x

    
    '''Converts article information to a dict and returns it'''

    def dictionary(self):
        x = dict({  'Id':self.no,
        'Embayment':self.embayment,
        'Article':self.title,
        'Author/s':self.auth,
        'Abstract':self.abstract,
        'Year':self.dateyear,
        'Link':self.link
        })

        return x 


'''A url class for converting user input into a url which can be requested using requests or urllib etc.'''
class url:

    def __init__(self, query, url="https://scholar.google.com.au/scholar?start={}&q="):
        
        '''Formats the input embayment and search terms to create the url for the search''' 
        queryTerms = query.strip().split(' ')
        separator ='+'
        prefix = url.format('00')

        self.prefix = prefix
        self.suffix = "&hl=en&as_sdt=0,5"
        self.terms  = separator.join(queryTerms)
        self.url    = self.prefix + self.terms + self.suffix


'''Class which takes in a url as an argument, requests it using requests, 
then converts it into a beautiful soup object, and returns the <body></body> section'''
class bsSchol:
    
    def __init__(self, url):
        self.html = requests.get(url, headers = {"User-Agent":"Mozilla/5.0"})
        self.soup = BeautifulSoup(self.html.content, "html.parser")
        self.body = self.soup.find("div", {"id":"gs_res_ccl_mid"})
        self.results = self.body.findAll("div", {"class":"gs_ri"})




#TODO: needs testing!!!
def scholarSpider(embDict):
    
    if type(embDict) != dict:
        raise AttributeError('Input must be dictionary')
    
    spiderOut = numpy.array(ndmin = 3)
    
    for embayment in embDict:
        embayment_query     = embayment
        extra_query_terms   = embDict[embayment]
        query               = embayment_query.strip() + " " + extra_query_terms.strip()
        search_url          = url(query)
        search_bsObj        = bsSchol(search_url.url)

        #Double square brackets required for the numpy.append call to append 
        #article_array in the for loop below.
        article_array = numpy.array([[
            "id",
            "Embayment",
            "Article Title",
            "Author/s",
            "Abstract",
            "Citations",
            "Link"]])

        #used to create a unique id within the numpy table. 
        number = 0

        for i in search_bsObj.results:
            entry = article(
                number,
                embayment_query,
                i)
            number += number

            article_array = numpy.append(article_array, entry.as_array(), axis=0)
        
        spiderOut = numpy.append(spiderOut, article_array, axis=2)
        
        '''Waits a random amount of time before collecting a new html'''
        time.sleep(random.randint(1,10) / random.random())
    return spiderOut
    
    
    
        
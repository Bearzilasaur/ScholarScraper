import requests
from urllib.error import HTTPError
from bs4 import BeautifulSoup
from os import system
import platform
import numpy as np
import time
import random


'''Article class for storing scraped information. Contains as_list method which returns the information as a list and as_dict which returns a dict'''
class article:
    def __init__(self, no, embayment, bsObj):
        
        
        self.no         = no
        self.embayment  = embayment
        self.title      = bsObj.find('h3', {'class':'gs_rt'}).text
        self.auth, self.dateyear   = bsObj.find('h3', {'class':'gs_ra'}).text.split('-')[0:2]
        self.abstract   = bsObj.find('div', {'class':'gs_rs'}).text
        self.citations  = bsObj.find('div', {'class': 'gs_fl'}).children[2].text
        self.link       = bsObj.find('h3', {'class':'gs_rt'}).a.get('href')
    
    '''Method which returns the information as a list with all the information stored in the class'''
    def as_array(self):
        x = np.array([
            self.no,
            self.embayment,
            self.title,
            self.auth,
            self.abstract,
            self.dateyear,
            self.link
        ])
        return x

    
    '''Converts information to a dict and returns it'''

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

class url:

    def __init__(self, query, url="https://scholar.google.com.au/scholar?start={}&q="):
        
        '''Formats the input embayment and search terms to create the url for the search''' 
        queryTerms = query.strip().split('')
        separator ='+'
        


        self.prefix = format(url, input('Start scraping at article number [00-99]:\n'))
        self.suffix = "&hl=en&as_sdt=0,5"
        self.terms  = separator.join(queryTerms)
        self.url    = self.prefix + self.terms + self.suffix

class bsSchol:
    
    def __init__(self, url):
        self.html = requests.get(url, headers = {"User-Agen":"Mozilla/5.0"})
        self.soup = BeautifulSoup(self.html, "html.parser")
        self.body = self.soup.find("div", {"id":"gs_res_ccl_mid"})
        self.results = self.body.findAll("div", {"class":"gs_ri"})




def scholarScrape():

    '''Asking for user input for scholar search'''
    embayment_query     = input("\n\nSearch:\n")
    extra_query_terms   = input("\n\nExtra Search Terms:\n")
    query               = embayment_query + " " + extra_query_terms
    search_url          = url(query)
    search_bsObj        = bsSchol(search_url.url)

    article_array = np.array([
        "id",
        "Embayment",
        "Article Title",
        "Author/s",
        "Abstract",
        "Citations"
        "Link"])

    
    number = 0
    for i in search_bsObj.results:
        entry = article(
            number,
            embayment_query,
            i)
        number += number
        article_array.append(entry)
    
    return article_array
        
'''======= Classes used in for the Scholar Scraper functions========='''

'''Author: Mitchell Baum'''
'''=================================================================='''

'''Article class for storing scraped information. Contains as_list 
#method which returns the information as a list and as_dict which 
#returns a dict'''

#TODO: DOCSTRING note triple apostrophe's are docstrings and are generally
#used for explaining what a piece of code does. Comments (#) should be 
#used to explain how something works or what it is doing. Need to go 
#through and edit all docstring into comments. '''

#'''required packages'''
from bs4 import BeautifulSoup
import numpy
import requests
import re

class article:
    def __init__(self, no, embayment, bsObj):
        
        
        self.no         = no
        self.embayment  = embayment
        self.title      = bsObj.find('h3', {'class':'gs_rt'}).text
        self.auth, self.dateyear= bsObj.find('div', {'class':'gs_a'}).text.split('-')[0:2]
        #TODO: ^^^ This method falls apart when any author has a '-' in 
        #their name. maybe use ' - ' instead as whitespace within 
        #hyphenated names is unlikely. 
        self.abstract   = bsObj.find('div', {'class':'gs_rs'}).text
        self.citations  = bsObj.find('div', {'class': 'gs_fl'}).find(text=re.compile("^Cited by"))
        self.link       = bsObj.find('h3', {'class':'gs_rt'}).find('a', href = True)['href']
    
    #Method which returns the information as a list with all the 
    #information stored in the class
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

    
    #Converts article information to a dict and returns it

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


#Class which sanitizes dictionary input to make sure that all 
#keys(embayments) are unique. 
#Taken from: https://stackoverflow.com/questions/5947950/how-can-i-force-a-dictionary-in-python-to-only-have-unique-keys
class UniqueDict(dict):
    def __setitem__(self, key, value):
        if key not in self:
            dict.__setitem__(self, key, value)
        else:
            raise KeyError("Key already exists")


#A url class for converting user input into a url which can be 
#requested using requests or urllib etc.
class url:

    def __init__(self, query, url="https://scholar.google.com.au/scholar?start={}&q="):
        
        #Formats the input embayment and search terms to create the 
        #url for the search'
        queryTerms = query.strip().split(' ')
        separator ='+'
        prefix = url.format('00')

        self.prefix = prefix
        self.suffix = "&hl=en&as_sdt=0,5"
        self.terms  = separator.join(queryTerms)
        self.url    = self.prefix + self.terms + self.suffix


#Class which takes in a url as an argument, requests it using requests, 
#then converts it into a beautiful soup object, and returns the 
#<body></body> section
class bsSchol:
    
    def __init__(self, url):
        self.html = requests.get(url, headers = {"User-Agent":"Mozilla/5.0"})
        self.soup = BeautifulSoup(self.html.content, "html.parser")
        self.body = self.soup.find("div", {"id":"gs_res_ccl_mid"})
        self.results = self.body.findAll("div", {"class":"gs_ri"})

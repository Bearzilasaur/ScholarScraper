'''
Scrapes google scholar search results and returns a numpy array of the 
first 10 results with the relevent information (authors, title, absract etc.)
=============================================================================
Author: Mitchell Baum
=============================================================================
'''
import requests
from bs4 import BeautifulSoup
import numpy
import re


'''Article class for storing scraped information. Contains as_list method which returns the information as a list and as_dict which returns a dict'''
class article:
    def __init__(self, no, embayment, bsObj):
        
        
        self.no             = no
        self.embayment      = embayment
        self.title          = bsObj.find('h3', {'class':'gs_rt'}).text
        (self.auth,         #TODO: this method using split does not work when an author has a '-' in their name maybe use ' - '??
        self.dateyear, 
        self.publication)   = bsObj.find('div', {'class':'gs_a'}).text.split('-')
        self.abstract       = bsObj.find('div', {'class':'gs_rs'}).text
        self.citations      = bsObj.find('div', {'class': 'gs_fl'}).find(text=re.compile("^Cited by"))
        self.link           = bsObj.find('h3', {'class':'gs_rt'}).find('a', href = True)['href']
    
    '''Method which returns the information as a list with all the information stored in the class'''
    def as_array(self):
        x = numpy.array([[
            self.no,
            self.embayment,
            self.title,
            self.auth,
            self.dateyear,
            self.publication,
            self.abstract,
            self.citations,
            self.link
        ]])
        return x

    
    '''Converts article information to a dict and returns it'''

    def dictionary(self):
        x = dict({  
        'Id':self.no,
        'Embayment':self.embayment,
        'Article':self.title,
        'Author/s':self.auth,
        'Year':self.dateyear,
        'Publication':self.publication,
        'Abstract':self.abstract,
        'Citations':self.citations,
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





def scholarScrape():

    '''Asking for user input for scholar search'''
    embayment_query     = input("\n\nSearch:\n")
    extra_query_terms   = input("\n\nExtra Search Terms:\n")
    query               = embayment_query + " " + extra_query_terms
    search_url          = url(query)
    search_bsObj        = bsSchol(search_url.url)

    article_array = numpy.array([[
        "id",
        "Embayment",
        "Article Title",
        "Author/s",
        "Year",
        "Publication",
        "Abstract",
        "Citations",
        "Link"]])

    
    number = 0

    for i in search_bsObj.results:
        entry = article(
            number,
            embayment_query,
            i)
        number += number

        article_array = numpy.append(article_array, entry.as_array(), axis=0)
    
    return article_array
        
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
    def __init__(self, no, embayment, htmlObj):
        
        
        self.no         = no
        self.embayment  = embayment
        self.title      = htmlObj.find('h3', {'class':'gs_rt'}).text
        self.auth, self.dateyear   = htmlObj.find('h3', {'class':'gs_ra'}).text.split('-')[0:2]
        self.abstract   = htmlObj.find('div', {'class':'gs_rs'}).text
        self.citations  = htmlObj.find('div', {'class': 'gs_fl'}).children[2].text
        self.link       = htmlObj.find('h3', {'class':'gs_rt'}).a.get('href')
    
    '''Method which returns the information as a list with all the information stored in the class'''
    def as_vector(self):
        y = []
        x = np.array([
            self.no,
            self.embayment,
            self.title,
            self.auth,
            self.abstract,
            self.dateyear,
            self.link
        ])
        for i in x:
            y.append(i)
        return y

    
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
        y = []
        for i in x:
            y.append(i)
        return y 

'''gets user query, formats the google sholar url and then retrieves the url to a BeautifulSoup object'''
def mkURL(embayment, query, custom = 'n', startpos = 00):
    
    '''Converts input embayment and search terms into suitable format for the generation of scholar url'''
    def srchConcat(embayment, other=None):
        srch =""     
        
        embTerms    = embayment.split()
        for i in embTerms:
            srch = srch + i + "+"

        if query != None:
            queryTerms  = other.split()
            for i in queryTerms:
                srch = srch + i +"+"

        srch = srch.strip("+")
        return srch

    if custom == 'y':
        startpos = input('\nInput number of search results to skip:\n')
    elif custom == 'n':
        pass
    else:
        custom = 'n'
        print('\n\n --~~**ERROR: Unable to parse custom search settings. No custom search performed.**~~--\n\n')
        time.sleep(7)



    '''Formats the URL'''
    bscPrefix   = "https://scholar.google.com.au/scholar?start={}&q="
    bscURL      = bscPrefix.format(int(startpos))
    bscSuffix   = "&hl=en&as_sdt=0,5"
    srch        = srchConcat(embayment, other=query)
    srchURL     = bscURL + srch + bscSuffix

    return srchURL


def getURL(url):
    try:
        html = requests.get(url, headers = {"User-Agent":"Mozilla/5.0"})
    except HTTPError as e:
        print(e)
    try:
        bsObj   = BeautifulSoup(html.content, "html.parser")
        arts    = bsObj.findAll('div', attrs={"class":"gs_res_ccl_mid"})
    #NOTE:^^^ arts is a LIST of search entries which needs to be iterated over. TODO: fix scholScrape to take in arts and treat it as a list TODO: fix article class to use .findChild to select specific elements from within each arts bs item.''' 

        return arts
    except AttributeError as e:
        print(e)


def scholScrape():


    '''Queries for the user input'''
    embSearch       = input('\n****Input embayment name:\n')
    embQuery        = input('\n****Input other query terms or leave blank if there are none:\n')
    customSearch    = 'y'   #input('\n****Would you like to custom search? [y/n]') <-TODO: implement a custom search feature
    noScrape        = input('\n****Input the number of scrapes')
        

    '''Generates the Url from user inputs for ScholBod(tests url and collect beautiful soup object)'''
    url = mkURL(embSearch, embQuery, custom=customSearch)

    '''Generates the numpy array in which the information will be stored'''


    '''Beautiful Soup Object which returns the search entries'''
    ScholBod = getURL(url)

    '''creating and filling out article classes for each entry in the search results'''
    def artParser(bsObj, emb_query, uniqueId = 0):
      #Iteration counter for id's
        arts = np.array([])
        count = 0
        for i in ScholBod:

            art = article(
                count,
                embSearch,
                i)
            count += count
            np.append(arts, art)
        return arts
    arts = artParser(ScholBod, embSearch)

    timeDelay = random.randrange(0, 20)
    time.sleep(timeDelay)
    return arts
    







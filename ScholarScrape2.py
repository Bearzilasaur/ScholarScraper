import requests
from urllib.error import HTTPError
from bs4 import BeautifulSoup
from os import system
import platform
import numpy as np
import time

'''Article class for storing scraped information. Contains as_list method which returns the information as a list'''
class article:
    def __init__(self, no, embayment, htmlObj):
        self.no         = no
        self.embayment  = embayment
        self.title      = htmlObj.find('h3', {'class':'gs_rt'}).text
        self.auth       = auth
        self.abstract   = abstract
        self.dateyear   = dateyear
        self.link       = link

    '''Method which returns the information as a list with all the information stored in the class'''
    def as_vector(self):
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
   
    '''prints out the format of the stored information'''
    def format(self):
        x = as_vector(self)
        for i in x:
            print(i)


'''Function clears the python interpreter console for cleaner user input'''
def clear():   
    x = platform.system()
    if x == 'windows':
        return system('cls')
    elif x == 'darwin':
        return system('clear')
    else:
        raise Exception('Unable to recognize system')

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
        clear()
        print('\n\n --~~**ERROR: Unable to parse custom search settings. No custom search performed.**~~--\n\n')
        time.sleep(7)
        clear()


    '''Formats the URL'''
    bscPrefix   = "https://scholar.google.com.au/scholar?start={}&q="
    bscURL      = bscPrefix.format(int(startpos))
    bscSuffix   = "&hl=en&as_sdt=0,5"
    srch        = srchConcat(embayment, other=query)
    srchURL     = bscURL + srch + bscSuffix

    return srchURL

def getURL(url):
    try:
        html = requests.get(url, headers = {"User-Agent":"Mozilla/5.0"}).text
    except HTTPError as e:
        print(e)
    try:
        bsObj   = BeautifulSoup(html.read())
        arts    = bsObj.findAll('div', attrs={"class":"gs_res_ccl_mid"}).children
        return arts
    except AttributeError as e:
        print(e)


def scholScrape():
    clear()

    '''Queries for the user input'''
    embSearch       = input('\n****Input embayment name:\n')
    embQuery        = input('\n****Input other query terms or leave blank if there are none:\n')
    customSearch    = input('\n****Would you like to custom search? [y/n]')
    noScrape        = input('\n****Input the number of scrapes')
        

    '''Generates the Url from user inputs for ScholBod(tests url and collect beautiful soup object)'''
    url = mkURL(embSearch, embQuery, custom=customSearch)

    '''Generates the numpy array in which the information will be stored'''
    output = np.array([])

    '''Beautiful Soup Object which returns the search entries'''
    ScholBod = getURL(url)

    '''Iteration counter for id's'''
    count = 0

    '''creating and filling out article classes for each entry in the search results'''
    for i in ScholBod:

        art = article(
            count,
            embSearch,
            i.

        )
        

     





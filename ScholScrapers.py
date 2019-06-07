'''
#---------------------------------------------------------------------
#Scrapes google scholar search results and returns a numpy array of the 
#first 10 results with the relevent information (authors, title, absract 
#etc.)
#=============================================================================
#Author: Mitchell Baum
#=============================================================================
'''





#Importing packages
import requests
from bs4 import BeautifulSoup
import numpy
import time
import random
import re
import sqlalchemy
import pandas as pd


#importing classes from ScholarClasses.py'''
from ScholarClasses import article, bsSchol, url, UniqueDict



#Takes a dict as input (?or two tuples) and scrapes google scholar for 
#each key:value pair. Intended use: pass an Embayment name as key and 
#keywords as values. Output in numpy format. 

#TODO: needs testing!!!
def scholarSpider(embDict):
    
    if type(embDict) != dict:
        raise AttributeError('Input must be dictionary')
    
    spiderOut = numpy.array([[
            "id",
            "Embayment",
            "Article Title",
            "Author/s",
            "Abstract",
            "Citations",
            "Link"]])
    
    for embayment in embDict:
        embayment_query     = embayment
        extra_query_terms   = embDict[embayment]
        query               = embayment_query.strip() + " " + extra_query_terms.strip()
        search_url          = url(query)
        search_bsObj        = bsSchol(search_url.url)

        #used to create a unique id within the numpy table. 
        number = 0

        for i in search_bsObj.results:
            entry = article(
                number,
                embayment_query,
                i)
            number += number

            spiderOut = numpy.append(spiderOut, entry.as_array(), axis=0)
        
        #Waits a random amount of time before collecting a new html
        time.sleep(random.randint(1,10))
    return spiderOut



#Takes user input and returns a numpy array with the releventa info
#from the first 10 results
def scholarScrape():

    #Asking for user input for scholar search
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



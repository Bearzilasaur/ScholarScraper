
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup as bs
import numpy as np
from time import sleep
from random import randint


#Tests whether or not html can be retrieved from the specified url and whether or not search results exist in the retrieved html and then returns the beautiful soup object
def getUrl(url):
    try:
        html = Request(url, headers= {"User-Agent":"Mozilla/5.0"})
        html2 = urlopen(html)
        print('Connection Successful')
    except HTTPError as e:
        print(e)
        print("Could not find specified site")
    try:
        bhtml = bs(html2.read())
        bhtml.find("", attrs={"id":"gs_res_ccl_mid"})
        return bhtml
    except AttributeError as e:
        print('Unexpected HTML format')




#concatenating the url with user provided search term and then appending with the appropriate url suffix once all term has been entered. 
#srchURL argument is the typical url structur for a google scholar search and suffix is the typical ending string, these can be modified by the user
def scholarConcat(embayment, searchterms, strt = 00 ,  srchUrl = "https://scholar.google.com.au/scholar?start=&q".format(str(strt)), suffix =  "&hl=en&as_sdt=0,5"):
    
    '''adds the embayment name to searchUrl and suffixes a '+' if other search terms are provided'''
    if isinstance(embayment, str):
        srchUrl = srchUrl + embayment
        if searchterms != None:
            srchUrl = srchUrl + "+"
    else:
        print('Embayment must be provided to scholarConcat in string format')
        break
    
    '''checks if extra search terms are provided and whether they are in the right format, then adds them to the search url'''
    if searchterms != '':
        if type(searchterms) == list:

            for i in srchtrms:
                i = strip(i)
                srchUrl = srchUrl + i +"+"
               
        else:
            print('Error: search terms passed to concatenator not in list form.')

    '''attaches the suffix to the search url and returns the search url'''
    srchUrl = srchUrl + suffix
    return srchUrl

'''asks user what entry they would like to start at and checks input to make sure it is formatted correctly.'''
def pg(start=00):
    pgstrt = input('\nWould you like to start at an entry other than 00? [y/n]\n')

    if pgstrt == 'y':
        strtart = input("\nPlease specify which entry you would like to start at (format: 00, 01, etc.)\n")
        start = strtart
        return start
    elif pgstrt == 'n':
        print('\nScrape will start at entry 00\n')
        return start
    else:
        print('\nPlease specify y or n\n')
        pg()

 
def scholarScrape(n=5):
    
    #request search terms
    srch = input('\nPlease input search as -> embayment name: search terms')\
    
    #split search terms into constituent parts
    embayment, srchtrms = srch.split(':')
    start = pg()

    url = scholarConcat(embayment, srchtrms, strt=start)
    bsObj = getUrl(url)

    '''initiates a numpy data frame in which to store the scraped information'''
    output = np.array(['id', 
    'embayment', 
    'ArticleTitle', 
    'Author/s', 
    'Date', 
    'Abstract',
    'Link',
    'Citations'
    ])
    
    '''iteration counter for for loop'''
    count = 0

    for each in bsObj.findAll('', attrs={"class":gs_ri}):
        for child in each.children:
            







    


    sleep(randint(3,8))
    pass

            








from scopus import ScopusSearch
import json

#Documentation can be found at https://scopus.readthedocs.io/en/stable/
#Author: Mitchell Baum

#TODO: Create scopus search functions for retrieval of basic information
#and for import of abstracts with scopArts and scopAbs. scopQuery used 
#to interface with scopus api using user input

def scopQuery(api="aba012f82a0a994632b6c8253eba6c91"):
    query   = input('\nPlease input your query:\n')
    #api     = input('\nPlease input your api key:\n') <- deprecated

    queryApi = query.replace('', '+') + '&apiKey=aba012f82a0a994632b6c8253eba6c91'  #format('&apiKey={}', api)
    srch = ScopusSearch(queryApi, view='STANDARD') #STANDARD View returs first 200
    jsrch = json.loads(srch)

    print(jsrch)

    return jsrch


#NOTE: Requires the article iD, maybe make a scopus article class and
#and call a scopQuery using to populate scopusarticle objects using the
#first 10 or so results. From that generate a list of scopusID's and
#then pass them to the scopus abstract retrieval api. This could all be
#it's own function similar to the scholar scraper. (see documentation
# for the python scopus wrapper, link at top of script)
#def scopAbs(n=10)







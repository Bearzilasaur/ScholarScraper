from scopus import ScopusSearch
import json

#Documentation can be found at https://scopus.readthedocs.io/en/stable/
#Author: Mitchell Baum

#TODO: Create scopus search functions for retrieval of basic information
#and for import of abstracts with scopArts and scopAbs. scopQuery used 
#to interface with scopus api using user input

def scopQuery(n=10, api="aba012f82a0a994632b6c8253eba6c91"):
    query   = input('\nPlease input your query:\n')
    #api     = input('\nPlease input your api key:\n') <- deprecated

    queryApi = query.replace('', '+') + format('&apiKey={}', api)
    srch = ScopusSearch(queryApi, count = n)
    jsrch = json.loads(srch)

    print(jsrch)

    return jsrch

def scopAbs(n=10)







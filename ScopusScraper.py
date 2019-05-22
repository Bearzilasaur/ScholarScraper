from scopus import ScopusSearch
import pandas as pd 
import json

#Documentation can be found at https://scopus.readthedocs.io/en/stable/
#Author: Mitchell Baum

def scopArts(n=10):
    query   = input('\nPlease input your query:\n')
    api     = input('\nPlease input your api key:\n')

    queryApi = query.replace('', '+') + format('&apiKey={}', api)
    srch = ScopusSearch(queryApi, count = n)
    jsrch = json.loads(srch)

    print(jsrch)

    return jsrch









import json
import requests

#Documentation for scopus module 
#can be found at https://scopus.readthedocs.io/en/stable/
#Author: Mitchell Baum

#TODO: Create scopus search functions for retrieval of basic information
#and for import of abstracts with fulltext and abstext. scopQuery used 
#to interface with scopus api using user input. 

#TODO: create an elsevier class for each article which contains the 
#important information??



#NOTE: scopQuery DOES NOT WORK, NEED TO FIX!!!!


def scopQuery(api="aba012f82a0a994632b6c8253eba6c91", sort='citations'):
    query   = input('\nPlease input your query:\n')
    queryForm = query.replace(' ', '%')
    prefix = 'https://api.elsevier.com/content/search/scopus?query='
    
    if sort == 'citations':
        suffix = '&httpAccept=application/json&count=10&subj=EART+ENVI&sort={}'.format('citedby-count')
    elif sort == 'relevance':
        suffix = '&httpAccept=application/json&count=10&subj=EART+ENVI&sort={}'.format('relevancy')
    else:
        raise AttributeError('sort option must be either "citations" or "relevance"')
    
    queryApi = prefix + queryForm + '&apiKey={}'.format(api) + suffix
    print(queryApi)

    srch = requests.get(queryApi) 
    jsrch = json.loads(srch.content)
    return jsrch


#NOTE: Requires the article iD, maybe make a scopus article class and
#and call a scopQuery using to populate scopusarticle objects using the
#first 10 or so results. From that generate a list of scopusID's and
#then pass them to the scopus abstract retrieval api. This could all be
#it's own function similar to the scholar scraper. (see documentation
# for the python scopus wrapper, link at top of script)

#def scopAbs(n=10)


#retrieves the full text of an article using the Elsevier API
#def scopText()




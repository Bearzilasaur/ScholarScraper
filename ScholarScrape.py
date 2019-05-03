from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup as bs


#Tests whether or not html can be retrieved from the specified url. 
def getUrl(url);
    try:
        html = urlopen(url)
        print('Connection Successful')
        return html
    except HTTPError as e:
        print(e)
        print("Could not find specified site")


#Tests whether or not the html contains the user specified tag
def tstHtml(url, tag):
    try:
        bhtml = bs(url.read())
        tsrch = bhtml.tag
    except AttributeError as e:
        print('Unexpected HTML format')


#request search terms
srch = input('Search Terms:')

#split search terms into constituent parts
srchtrms = srch.split()



#concatenating the url with user provided search term and then appending with the appropriate url suffix once all term has been entered. 
#srchURL argument is the typical url structur for a google scholar search and suffix is the typical ending string, these can be modified by the user
def scholarConcat(searchterms, srchUrl = "https://scholar.google.com.au/scholar?hl=en&as_sdt=0%2C5&q=", suffix = "&btnG="):
    #iteration counter
    count = 0


        if type(searchterms) == list:

            for i in srchtrms:
                count = +
                i = strip(i)
                srchUrl = srchUrl + i +"+"
                if count = len(srchtrms):
                    srchUrl = srchUrl + 
                    return srchUrl
                    print(srchUrl)
        else:
            print('Error: search terms passed to concatenator not in list form.')








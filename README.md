# ScholarScraper
Repository for a Google Scholar scraper for literature reviews. 


Notes on the install of scopus using Conda

When using the scopus package for the first time it will set up a ~/.scopus/config.ini file.

The scopus package requires that a framework python is used to set this up.
However, conda environments do not implement a framework python.
See https://matplotlib.org/faq/osx_framework.html for more information.

To set up a framework python within a conda environment simply use:

	local$host: conda install python.app

Next, open the framework python with 'pythonw'.
Finally, import the scopus package into the interpreter, and follow the prompts to set up a ~/.scopus/config.ini file. 



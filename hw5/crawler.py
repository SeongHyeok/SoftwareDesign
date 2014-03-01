# -*- coding: utf-8 -*-
"""
Simple Web Crawler for HW5

Created on Fri Feb 28 15:14:04 2014

@author: SeongHyeok Im
"""

#############################################################################
# Imports
#############################################################################

import urllib
import re
import sys

#############################################################################
# Global variables
#############################################################################

# Regular expression for extracting link from 'a href'
regex_1 = r'href=[\'"]?([^\'" >]+)'

# Exclude extension list
allowed_protocols = ['http://', 'https://']
exclude_extensions = ['.css', '.jnz', '.ico', ]
index_names = ['default.aspx', 'index.htm', 'index.html', 'index.php']

olin.edu
www.olin.edu
http://www.olin.edu/
http://olin.edu/
olin.edu/default.aspx

#############################################################################
# Functions
#############################################################################

def fetch_link_urls(url):
    """
    """
    data = urllib.urlopen(url).read()
    found_urls = re.findall(regex_1, data)
    return found_urls

def test_fetch_link_urls():
    """
    """
    test_urls = ["http://www.olin.edu"]
    for test_url in test_urls:
        urls = fetch_link_urls(test_url)
        fetched_urls = []
        for url in urls:
            if url[0] == "#":
                continue
            elif url[0] == "/":
                fetched_urls.append(test_url + url)
            else:
                fetched_urls.append(url)
        fetched_urls = list(set(fetched_urls))  # remove duplicates
        print "Test: fetch_link_urls(%s) ==========" % (test_url)
        print "Number of urls: %d" % (len(fetched_urls))
        print "Results:"
        for url in fetched_urls:
            print url


def do_crawl(url):
    """
    """
    return


def convert_url(url):
    """ Converts given url to the specifically defined form of url.
        Note that it doesn't append base url to the beginning of given url.
    """    
    # protocol
    check = False
    pos_p = 0
    for protocol in allowed_protocols:
        l = len(protocol)
        if url[0:l] == protocol:
            check = True
            pos_p = l
            break
    if check == False:
        url = allowed_protocols[0] + url
        pos_p = len(allowed_protocols[0])
        
    # add 'www.'
    www = "www."
    idx = url.find(www)
    if idx == -1:
        url = url[0:pos_p] + www + url[pos_p:]
    
    # last slash
    if url[-1] == '/':
        url = url[:-1]
    
    return url

def test_convert_url():
    """ Tests convert_url()
    """
    test_data = [
        ["http://www.olin.edu", "http://www.olin.edu"],
        ["www.olin.edu", "http://www.olin.edu"],
        ["http://olin.edu", "http://www.olin.edu"],
        ["olin.edu", "http://www.olin.edu"],
        # last slash
        ["http://www.olin.edu/", "http://www.olin.edu"],
        ["www.olin.edu/", "http://www.olin.edu"],
        ["http://olin.edu/", "http://www.olin.edu"],
        ["olin.edu/", "http://www.olin.edu"],
        #
    ]
    for data in test_data:
        if len(data) == 2:
            result = convert_url(data[0])
            print "Test: convert_url(\"%s\") ==========" % (data[0])
            print "Result: %s" % result
            if result != data[1]:
                print "## Test Fail Here!!"

def input_url():
    """
    """
    print "Enter URL to crawl: "
    url = convert_url(raw_input("> "))
    if url == None:
        print "[Error] Invalid URL"
        sys.exit(1)
    return url
        
if __name__ == "__main__":
    #test_convert_url()
    test_fetch_link_urls()
    
    #do_crawl(input_url())
# -*- coding: utf-8 -*-
"""
Simple Web Crawler for HW5

@date: Fri Feb 28 15:14:04 2014
@author: SeongHyeok Im
@detail:
    This python script crawls webpages from given url.
    1. Fetch webpage data from given url.
    2. Extract link urls from fetched data.
    3. Standardize all urls and remove duplicates.
    4. Fetch webpage data from all standardized urls and save to a file.
       (Hierarchical structure is remained as directories)

@to-do-in-future:
    - Extract domain automatically.
    - Enhance url standardization method.
    - Visit webpages recursively.
        - Set depth of visit.
        - Check already visited webpage.
    - Crawl pages using multi-thread for better performance.
"""

#############################################################################
# Imports
#############################################################################

import urllib
import re
import sys
import os
import time

#############################################################################
# Global variables
#############################################################################

# Regular expression for extracting link from 'a href'
# reference: http://stackoverflow.com/questions/499345/regular-expression-to-extract-url-from-an-html-link
regex_1 = r'href=[\'"]?([^\'" >]+)'


allowed_protocols = ['http://', 'https://']

# Exclude extension list
exclude_extensions = ['.css', '.jnz', '.ico', ]
exclude_words = ['mailto:']

index_names = ['/Pages/home.aspx', 'default.aspx', 'index.htm', 'index.html', 'index.php']
# Babson websites blocks /Pages but not /Pages/home.aspx

data_file_name = "data.txt"

#############################################################################
# URL Functions
#############################################################################

def fetch_link_urls(url, domain):
    """ Fetch all link urls from given url.

        url: url of webpage to be fetched
        domain: scope of result urls, urls which include this domain will be returned
    """
    page_data = urllib.urlopen(url).read()
    found_urls = re.findall(regex_1, page_data)
    result = []

    for found_url in found_urls:
        #print "found: %s" % (found_url)
        processed_url = ""

        # check exclusion
        chk = False

        for word in exclude_words:
            if word in found_url:
                chk = True
                break
        if chk: continue

        for ext in exclude_extensions:
            if ext in found_url:
                chk = True
        if chk: continue

        if found_url[0] == "#":
            continue

        # check relative path url
        if found_url[0] == "/":
            processed_url = url + found_url
        elif found_url[:2] == "./":
            processed_url = url + found_url[1:]  # remove '.'
        else:
            processed_url = found_url

        # remove name of index page from url
        for index_name in index_names:
            if processed_url.endswith(index_name) or processed_url.endswith(index_name + '/'):
                processed_url = processed_url.split(index_name)[0]
                break

        processed_url = convert_url(processed_url)

        # final url check
        if processed_url.count('.') == 0:
            continue
        # check domain
        if processed_url.count(domain) == 0:
            continue

        result.append(processed_url)
        #print "proc : %s" % (processed_url)

    result = list(set(result))    # remove duplicates

    return result

def test_fetch_link_urls():
    """ Tests fetch_link_urls()
    """
    test_data = [
        ["http://www.olin.edu", "olin.edu"],
        ["http://www.babson.edu", "babson.edu"],
        ["http://www.wellesley.edu", "wellesley.edu"],
    ]
    for test_url, test_domain in test_data:
        fetched_urls = fetch_link_urls(test_url, test_domain)
        print "Test: fetch_link_urls(%s, %s) ==========" % (test_url, test_domain)
        print "Number of urls: %d" % (len(fetched_urls))
        print "Results:"
        for url in fetched_urls:
            print url

def convert_url(url):
    """ Converts given url to the specifically defined form of url.
        Note that it doesn't append base url to the beginning of given url.
    """
    # add protocol
    check = False
    pos_p = 0   # position of protocol
    for protocol in allowed_protocols:
        l = len(protocol)
        if url[0:l] == protocol:
            check = True
            pos_p = l
            break
    if check == False:
        url = allowed_protocols[0] + url
        pos_p = len(allowed_protocols[0])

    # remove last slash
    if url[-1] == '/':
        url = url[:-1]

    # add 'www.'
    www = "www."
    idx = url.find(www)
    if idx == -1:
        # if http://A.B such as http://olin.edu/
        #   then add www. hence it becomes http://www.olin.edu
        # if http://A.B.C such as http://scope.olin.edu then doesn't add.
        if url.count('.', pos_p, url.find('/', pos_p + 1)) == 1:
            url = url[0:pos_p] + www + url[pos_p:]

    return url.lower()

def test_convert_url():
    """ Tests convert_url().
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
        # different subdomain
        ["olingear.olin.edu", "http://olingear.olin.edu"],
        ["scope.olin.edu", "http://scope.olin.edu"]
    ]
    for data in test_data:
        if len(data) == 2:
            result = convert_url(data[0])
            print "Test: convert_url(\"%s\") ==========" % (data[0])
            print "Result: %s" % result
            if result != data[1]:
                print "## Test Fail Here!!"

#############################################################################
# Main functions
#############################################################################

def input_url():
    """ Input url from user.
    """
    print "Enter URL to crawl(if omit, olin.edu): "
    url = raw_input("> ")
    if url == "":
        url = "olin.edu"
    url = convert_url(url)
    if url == None:
        print "[Error] Invalid URL"
        sys.exit(1)
    print "Processed URL:", url
    return url

def input_domain():
    """ Input domain from user
    """
    print "Enter Domain for crawling(if omit, olin.edu): "
    domain = raw_input("> ")
    if domain == "":
        domain = "olin.edu"
    return domain

def do_crawl(url, domain):
    """ Main crawling function.
    """
    # Backup current path
    prev_path = os.curdir

    # Create root directory
    lt = time.localtime()
    dir_name = "%02d%02d%04d-%02d%02d%02d" % \
    (
        lt.tm_mon, lt.tm_mday, lt.tm_year, lt.tm_hour, lt.tm_min, lt.tm_sec
    )
    root_path = os.path.join(os.curdir, dir_name)
    os.mkdir(root_path)

    # Create domain directory in the root directory
    domain_path = os.path.join(root_path, domain)
    os.mkdir(domain_path)
    #os.chdir(domain_path)

    # Get links
    all_urls = fetch_link_urls(url, domain)

    # Get pages
    l = len(all_urls)
    for i in range(l):
        url = all_urls[i]

        # Print progress
        print "[%d/%d]" % (i + 1, l)

        # Create directory for saving file
        file_path = os.path.join(domain_path, url)
        os.system("mkdir -p %s" % (file_path))

        # Save webpage to a file
        f = file(os.path.join(file_path, data_file_name), 'wt')
        f.write(urllib.urlopen(url).read())
        f.close()

    # Recover previous working path
    os.chdir(prev_path)
    return

#############################################################################
#
#############################################################################

if __name__ == "__main__":
    #test_convert_url()
    #test_fetch_link_urls()

    url = input_url()
    domain = input_domain()
    do_crawl(url, domain)
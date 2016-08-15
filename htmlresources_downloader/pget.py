#!/usr/bin/env python

''' This script helps me download all available resources and documents
    mentioned on an URL.
'''

import sys
import urllib
import pycurl
import argparse
import time
import os
from bs4 import BeautifulSoup

def main():

    url = ""
    listTypes = []
    folderName = ""
    start_time = ""

    # Setting parser.
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="The url of the files")
    parser.add_argument("-fn", "--foldername",
            help="the files will be downloaded to this newly created folder")
    parser.add_argument("-v", "--verbosity", action="store_true",
            help="Increase output verbosity")
    parser.add_argument("-q", "--quiet", action="store_true",
            help="Show no standard output.")
    parser.add_argument("-ft", "--filetypes", nargs="+",
            help="List the file extensions you want to download.")
    args = parser.parse_args()

    # Gathering and assigning command line arguments to local variables.
    url = args.url

    if (args.filetypes):
        filetypes = ' '.join(args.filetypes)
        listTypes = args.filetypes
        print "[*] List file types: " + filetypes

    if (args.foldername):
        folderName = args.foldername
        if not os.path.exists(folderName):
            os.makedirs(folderName)

    print "[*] Fetching resources from destination: " + url + "..."
    if "http://" not in url:
        refined_url = "http://" + url

    response = urllib.urlopen(refined_url).read()

    soup = BeautifulSoup(response, "lxml")

    for a_tag in soup.find_all('a', href=True):
        a_href = a_tag['href']
        if url in a_href and checkTypes(listTypes, a_href):
            if not start_time:
                start_time = time.time()

            filename = getFileInUrl(a_href)
            if args.verbosity:
                print "[*] Downloading: ", filename

            fp = open("./"+folderName+"/"+filename, "wb")
            curl = pycurl.Curl()
            curl.setopt(pycurl.URL, a_href)
            curl.setopt(pycurl.WRITEDATA, fp)
            curl.perform()
            curl.close()
            fp.close()

    if (start_time):
        print "[*] Done! Total time: ", (time.time() - start_time)
    else:
        print "[*] No file to download. Exiting."
        os.rmdir(folderName)
        sys.exit()

def checkTypes(listTypes, s):
    if len(listTypes) == 0:
        return True

    for t in listTypes:
        if t == s[len(s) - len(t):]:
            return True
    return False

def getFileInUrl(s):
    s_list = s.split('/')
    return s_list[len(s_list) - 1]

if __name__ == "__main__":
    main()

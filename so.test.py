import urllib2
import sys
import re
msg = sys.argv[1]

def stackoverflow(msg):
    sourl = "http://stackoverflow.com/"
    if msg == "":
        return "Please give a query"
    else:
        a = msg[:15]
        print(a)
        site = (sourl + "search?q=" + a)
        hdr = {'User-Agent': 'Mozilla/5.0'}
        req = urllib2.Request(site,headers=hdr)
        page = urllib2.urlopen(req)
        soq = page.readlines()
        for line in soq:
            if "Q:" in line:
                print(line)
        page = urllib2.urlopen(req)
        soex = page.readlines()
        line = ['']
        for line in soex:
            if "excerpt" in line:
                print(line)
stackoverflow(msg)

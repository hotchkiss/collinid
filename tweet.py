#!/usr/bin/env python
import urllib
import webbrowser
import sys

def main():
    #Open webpage with tweet intent for the passed parameter
    url = 'http://twitter.com/intent/tweet?text='
    text = urllib.quote(sys.argv[1], '')
    url += text
    webbrowser.open_new_tab(url)

if __name__=="__main__":
    main()

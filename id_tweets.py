#!/usr/bin/env python
import sys
import random
import os

bad_things = ["words to redact go here"]

def check_tweets(words):
    """using this shit to check for bad things I don't want to tweet to strangers lol"""
    print words
    for a in bad_things:
        if words.find(a) != -1:
            return False
    return True

def main():
    fopen = open("""path to file with keylogged data""")
    f = fopen.read()
    previous = open("""path to file of previously tweeted phrases""", 'r+')
    start = random.randint(0,int(len(f)))
    sample_tweet = f[start:start+random.randint(90, 140)]
    already = previous.read()
    while not check_tweets(sample_tweet):
        start = random.randint(0,int(len(f)))
        sample_tweet = f[start:start+random.randint(90,140)]
    previous.write(str(start) +"\n" + sample_tweet + "\n")
    sample_tweet = "\"" + sample_tweet + "\""
    #Give a web intent prompt for the current sample_tweet
    os.system("python /Users/collinhotchkiss/Dropbox/LitTech/tweet.py " + sample_tweet)
    previous.close()
    sys.exit(0)

if __name__ == '__main__':
    main()

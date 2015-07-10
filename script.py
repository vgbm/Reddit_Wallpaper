import praw
import requests
import os
#from bs4 import BeautifulSoup

#needs feh, praw, and requests installed

r = praw.Reddit(user_agent='example')
submissions = r.get_subreddit('animewallpaper').get_top(limit=20)

subList = [sub for sub in submissions] #list of submissions
target = subList[0] #target is the goal picture; defaults to the first option
resolution = "1920x1080" #target resolution
resolution2 = "1920X1080"

for sub in subList:
    if (resolution in sub.title or resolution2 in sub.title) and '/a/' not in sub.url and 'imgur' in sub.url:
        target = sub
        break

url = target.url
if '.jpg' not in url:
    url += '.jpg'

f = open('/home/james/Pictures/background.jpg','wb')
f.write(requests.get(url).content)
f.close()

#feh -bg-fill $path/to/file
os.system('feh --bg-fill /home/james/Pictures/background.jpg')

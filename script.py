import praw
import requests
#from bs4 import BeautifulSoup

#needs hsetroot installed

r = praw.Reddit(user_agent='example')
submissions = r.get_subreddit('animewallpaper').get_top(limit=10)

subList = [sub for sub in submissions] #list of submissions
target = subList[0] #target is the goal picture; defaults to the first option
resolution = "1920x1080" #target resolution


for sub in subList:
    if resolution in sub.title and '/a/' not in sub.url:
        target = sub
        break

url = target.url
if '.jpg' not in url:
    url += '.jpg'

f = open('/home/vgbm/Pictures/background.jpg','wb')
f.write(requests.get(url).content)
f.close()

#hsetroot -fill $path/to/file

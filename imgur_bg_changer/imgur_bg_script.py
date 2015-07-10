import urllib
import requests
import os
import sys


def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start


albumInfo = [line.strip('\n') for line in open("album").readlines()]
print albumInfo

if len(albumInfo) < 2:
    sys.exit("album file is missing information; needs \nurl\nsize of album\nimage path")

album_url = albumInfo[0]
path = albumInfo[1]

#getting direct links from page source to set jpg
img_links = [line if "meta property=\"og:image\"" in line else "" for line in urllib.urlopen(album_url)]
img_links = [link.strip() for link in filter(lambda x: x != '', img_links)]
img_links = [link[find_nth(link,'"',3)+1:find_nth(link,'"',4)] for link in img_links]

while True:

    
    bg_command = 'feh --bg-fit '+path
    os.system(bg_command)

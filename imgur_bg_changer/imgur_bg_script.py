import urllib
import requests
import os
import sys
import random
import time

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

#getting direct links from page source to set jpg
def get_img_links(album_url):
    img_links = [line if 'meta property="og:image"' in line else '' for line in urllib.urlopen(album_url)]
    img_links = [link.strip() for link in filter(lambda x: x != '', img_links)]
    img_links = [link[find_nth(link,'"',3)+1:find_nth(link,'"',4)] for link in img_links]
    return img_links


albumInfo = [line.strip('\n') for line in open("album").readlines()]

if len(albumInfo) < 4:
    sys.exit("album file is missing information; it needs:: \n\t1) url to base album\n\t2) image save path\n\t3) rotation delay minimum\n\t4) desired command to set background image")

album_url = albumInfo[0]
path = albumInfo[1]
delay = int(albumInfo[2])
command = albumInfo[3]

bg_command = command+' '+path
img_links = get_img_links(album_url)

curr_link = random.choice(img_links)
while True:
    
    prev_link = curr_link
    curr_link = random.choice(img_links)
    while prev_link==curr_link:
        curr_link = random.choice(img_links)
  
    #this causes a delay of several seconds for large images
    #less noticeable for longer periods, but
    #quite noticeable for < ~20 seconds
    
    
    f = open(path,'wb')
    f.write(requests.get(curr_link).content)
    f.close()
    
    
    os.system(bg_command)
    
    time.sleep(delay)

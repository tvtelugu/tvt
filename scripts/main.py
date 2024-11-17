import requests
import os
import sys

CHANNEL_LIST='../channel_list.txt'

def url_grabber(url): 
    """Function to get the m3u8 link from a youtube video"""
    response = requests.get(url, timeout=15).text
    #Encuentra donde esta el .m3u8 y anadele 5 espacios para incluir el .m3u8
    end = response.find('.m3u8') + 5 
    tunner = 100

    while True:
        if 'https://' in response[end-tunner : end]:
            link = response[end-tunner : end]
            start = link.find('https://')
            end = link.find('.m3u8') + 5
            break
        tunner += 5
    print(f"{link[start : end]}")

with open(CHANNEL_LIST) as file:
    for line in file:
        line = line.strip()
        if not line or line.startswith('~~'):
            continue
        if not line.startswith('https'):
            line = line.split('|')
            chanel_name = line[0].strip()
            group_title = line[1].strip().strip()
            tvg_logo = line[2].strip()
            tvg_id = line[3].strip()
            print(f'\n#EXTINF:-1 group-title="{group_title}" tvg-logo="{tvg_logo}" tvg-id="{tvg_id}", {chanel_name}')
        else:
            url_grabber(line)

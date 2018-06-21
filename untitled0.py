#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 11:10:30 2018

@author: heyo
"""

import urllib.request
import json
from pprint import pprint
import requests

def read_web_json(link):
    with urllib.request.urlopen(link) as url:
        data = json.loads(url.read().decode())
    return data
    
def read_local_json(filename):
    with open(filename) as data_file:    
        data = json.load(data_file)
    return data

def get_keys(data):
    return data.keys()

def read_html(link):
    r = requests.get(link)
    html = r.text
    return html

def count_line(doc):
    num_lines = sum(1 for line in open(doc))
    return num_lines

def get_json_links(data):
    """ klasördeki json'ın içerisindeki json linklerini çeker"""
    json_list = []
    for dic in data:
        json_list.append(dic['link'])
    return json_list


def get_links_in_json(json_list):
    """ Çekilen json linklerindeki haberleri çeker """
    web_json_list = []
    for idx, webdic in enumerate(json_list):
        print(str(idx) + "/" + str(len(json_list)) )
        web_json = read_web_json(webdic)
        for wj in web_json['data']:
            web_json_list.append(wj['link'])
    return web_json_list


def write_html(link):
    for idx, site in enumerate(link):
        try:
            write_file = open("news" + str(idx) + ".txt" , "w")
            html = read_html(site)    
            write_file.write(html)
            write_file.close()
        except:
            pass



data = read_local_json("2007.json")
data = data['data']
json_links = get_json_links(data)
web_json_links = get_links_in_json(json_links)




"""
from multiprocessing.dummy import Pool as ThreadPool
pool = ThreadPool(16)
result = pool.map(write_html, links)


new_data = data[:20]
"""

""" guid id'ye göre directory oluşturup içerisine json'ı yazıyor """
import os
for val in data:
    title = val['guid']
    json_link = val['link']
    """ 
    s = list(title)
    for idx, cha in enumerate(s):
            if cha == "/":
                s[idx] = "." 
    "".join(s)
    """    
    os.mkdir(title)
    os.chdir(title)
    read_json = read_web_json(json_link)
    write_json = open(str(title) + ".json", "w")
    dump_dict = json.dumps(read_json)
    write_json.write(dump_dict)
    write_json.close()
    os.chdir("..")


""" guid ve json'ın içindeki linkleri csv'ye yazdırıyor """
with open('eggs.csv', 'w', newline='') as csvfile:

    for idx, val in enumerate(data):
        title = val['guid']
        json_link = val['link']
        """ 
        s = list(title)
        for idx, cha in enumerate(s):
                if cha == "/":
                    s[idx] = "." 
        "".join(s)
        """    
        print(str(idx) + "/" + str(len(data)))
        
        read_json = read_web_json(json_link)
    
        for links in read_json['data']:
            spamwriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow([title, links['link']])



    
    
    
heyo = "asd"
import csv
with open('eggs.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow([heyo])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
    




title = "////"
s = list(title)
for idx, cha in enumerate(s):
    if cha == "/":
        s[idx] = "."
"".join(s)

        



""" Çekilen json linklerindeki haberleri çeker """
web_json_list = []
new_json_list = json_list[:8]
for webdic in json_list:
    web_json = read_web_json(webdic)
    for wj in web_json['data']:
        web_json_list.append(wj['link'])
    

file = open("2007_newlink.txt","w")

for link in links:
    file.write(link + "\n")
    
file.close()
    



for idx, site in enumerate(web_json_list):
    try:
        write_file = open("news" + str(idx) + ".txt" , "w")
        html = read_html(site)    
        write_file.write(html)
    except:
        pass








pprint(data.keys())


pprint(data['data'])

new_data = data['data']
pprint(len(new_data))
pprint(new_data[0])
pprint(type(new_data))


first_data = new_data[0]
link = first_data['link']


web_json = get_web_json(link)

l = []
type(l)
type(new_data)

heyo = read_local_json("2007.json")
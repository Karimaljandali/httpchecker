########################################
#        Made by Karim Aljandali       #
#              07-17-18                #
########################################

import requests
import os
import contextlib
import csv

with contextlib.suppress(FileNotFoundError): #Delete http-results.csv if it exists already, don't want duplicate data if we have to run again.
    os.remove("http-results.csv")

with open('http-results.csv','w', newline='', encoding="utf-8") as csv_file: #rename csv file to website name.csv
		writer = csv.writer(csv_file)
		writer.writerow(["Input", "HTTP Response", "Output"]) #Write header
#This must be added to requests to prevent all requests from being 403.
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
f = open('sites.txt', 'r')
links = [links.strip() for links in f.read().split(',')] #List comprehension, strip textfile and grab all links.
for link in links:
    test = requests.get(link, headers=headers) #Make request
    for temp in test.history:
        with open('http-results.csv', 'a', newline='', encoding="utf-8") as csv_file:  # rename csv file to website name.csv
            writer = csv.writer(csv_file)
            writer.writerow([link,test.history,test.url])
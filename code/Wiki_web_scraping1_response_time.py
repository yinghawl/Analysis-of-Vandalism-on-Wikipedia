# -*- coding: utf-8 -*-
"""
Created on Tue Dec 01 14:16:27 2015
To get the time it took to revert an edit.
@author: YingHaw
"""

##Import all the required packages
import csv
import mwclient
from time import mktime


#Read in the data from 5000 most viewed list and store the pages name as a list
wikipage=list()
NumRev=list()
pageRev=dict()

#Open "Wiki_final1.csv" (the preprocessed data) and read in the page titles and the number of reverted edits
with open('Wiki_final1.csv') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
         if int(row['Number.of.reverted.edits']) ==0: continue #Run the page if there is more than one reverted edits
         pageRev[row['Page.Title']]=int(row['Number.of.reverted.edits'])

#Get the revid and the time that the edit was reverted
timeafter=dict() #which consists of the parentid of the reverted edit and the time the edit was made
 # whcih consists of the revid of the original edit and the time the original edit was mde

#Output a new csv file with page name and its associated protection status,number of edits and number of vandalisms
with open('Wiki_timedata1.csv', 'w') as csvfile:
    fieldnames = ['Page Title', 'Average response time(seconds)']
    writer = csv.DictWriter(csvfile, lineterminator='\n',fieldnames=fieldnames)
    writer.writeheader()
    i=0
    for key in pageRev:
        site = mwclient.Site('en.wikipedia.org')
        page = site.Pages[key]
        pageview= page.text()
        revisions = page.revisions(start='2015-11-15T00:00:00Z',
                           end='2015-11-21T23:59:59Z',
                           dir='newer',
                           prop='ids|timestamp|comment|user')
        ####Run iteration to look for all the reverted edits and its associated time
        itercount=0
        for counter in range(100000):
            try:
                rev = revisions.next()
                #pprint(rev)
                if  "Revert" in rev["comment"]:
                    timeafter[rev['parentid']]=mktime(rev['timestamp'])
                    icount = icount + 1
            except: break

        #Rerun the revision pages for a longer duration just in case there are some edits which were made before the start date
        revisions = page.revisions(start='2015-11-01T00:00:00Z',
                           end='2015-11-21T23:59:59Z',
                           dir='newer',
                           prop='ids|timestamp|comment|user')

        #####Run iteration to look for the original edit and compute the time difference
        count=0
        timediff=list()
        for counter in range(100000):
            try:
                rev=revisions.next()
                if rev["revid"] in timeafter.keys():
                    timediff.append(timeafter[rev["revid"]]-mktime(rev["timestamp"])) #compute the difference in time in second
            except:
                break
        timeaverage= sum(timediff)/pageRev[key]

        writer.writerow({'Page Title': key, "Average response time(seconds)":timeaverage})
        print i
        i+=1

            
    

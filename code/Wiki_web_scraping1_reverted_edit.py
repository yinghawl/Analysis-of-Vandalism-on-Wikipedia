# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 17:34:30 2015

@author: YingHaw
"""
##Import all the required packages
import csv
import mwclient


     
#Read in the data from 5000 most viewed list and store the pages name as a list
wikipage=list()
with open('Wikipedia_5000_Most_Viewed.csv') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
         wikipage.append(row['Page Title'])
         
accentpage=list()
for i in range(len(wikipage)):
     try:
         print i
         site = mwclient.Site('en.wikipedia.org')
         page = site.Pages[wikipage[i]]
     except:
         accentpage.append(wikipage[i])
         continue

##Output a new csv file with page name and its associated protection status,number of edits and number of vandalisms

with open('Wikidata.csv', 'w') as csvfile:
    fieldnames = ['Page Title', 'Number of reverted edits','Number of edits','Status']
    writer = csv.DictWriter(csvfile, lineterminator='\n',fieldnames=fieldnames)

    writer.writeheader()
     
    for i in range(len(wikipage)):
        num=2425
        print i + num
        #if i in [23,30,130,137,191,269,290,313,460,557,577,605,739,793,837,846,884,926,938,973,1016,1024,
        #1105,1114,1131,1142,1143,1197,1199,1250,1345,1430]: continue
        
        
        if wikipage[i] in accentpage: continue
        
        site = mwclient.Site('en.wikipedia.org')
        page = site.Pages[wikipage[i+num]]
        pageview= page.text()
        revisions = page.revisions(start='2015-11-01T00:00:00Z',
                           end='2015-11-30T23:59:59Z',
                           dir='newer',
                           prop='ids|timestamp|comment|user')
        
        """Checking whether it is semi-protected"""
        semiprotect= pageview.find('pp-vandalism') + pageview.find('pp-semi')+pageview.find('pp-move')
        if semiprotect <= -1:
            semiprotect = 0
        else: semiprotect = 1
      
      
        
        """Counting the number of vandalisms and edits"""
        
        RevED=0
        NumED=0
        
        for counter in range(100000):
            try:
                NumED +=1
                rev = revisions.next()
           
                if  "Revert" in rev["comment"]: 
                    RevED = RevED + 1
                
            except: break
   
        writer.writerow({'Page Title': wikipage[i+num], 'Number of reverted edits': RevED, 'Number of edits': NumED,'Status' : semiprotect})


 




#parentid=list()
#time_after=list()
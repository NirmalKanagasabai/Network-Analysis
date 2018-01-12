import urllib2
import socket
from bs4 import BeautifulSoup
import pandas as pd
import csv
import time


url_list = <<This list is populated by reading a .csv file which was sent as an ouput from Infinite_Scrolling.py"

#url_list = []
A=[]
B=[]
C=[]
D=[]
E=[]
cells = []

for row in url_list:
    try:
        page_source = urllib2.urlopen(row)
    except urllib2.URLError:
        print ("Exception - "+row)
        continue

    if "xxx" in row:
        print("XXX - "+row)
    else:
        soup = BeautifulSoup(page_source.read().decode('utf-8', 'ignore'), 'html.parser')
        print soup.title
        try:
            table = []
            table = soup.find('div',attrs={"id":"ff-dating-history-table"}).findAll('table')
        except Exception:
            pass

        if len(table) == 0:
            print "Empty list"
            continue

        for row in table[0].findAll("tr"):
            cells = row.findAll('td')
            if len(cells)==8:
                A.append(cells[1].find(text=True))
                B.append(cells[2].find(text=True))
                C.append(cells[4].find(text=True))
                D.append(cells[5].find(text=True))
                if soup.topic is None:
                    E.append(soup.title)
                else:
                    E.append(soup.topic.text)

        df = pd.DataFrame(A, columns=['Partner'])
        df['Type']=B
        df['Start']=C
        df['End']=D
        df['Celebrity']=E

        filename = '<<Path to CSV>>/Relationships.csv'

        with open(filename, 'a') as f:
            df.to_csv(filename, index=False, encoding='utf-8')
            print "done"

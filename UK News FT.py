import sklearn
import numpy as np
import pandas as pd 
from datetime import date

import xml.etree.cElementTree as et
import requests

def getvalueofnode(node):
    """ return node text or None """
    return node.text if node is not None else None

def main(URL):
    response = requests.get(URL)
    with open('test.xml', 'wb') as file:
    	file.write(response.content)
    parsed_xml = et.parse("test.xml")
    dfcols = ['title','description','link']
    df_xml = pd.DataFrame(columns=dfcols)
    for node in parsed_xml.find('channel'):
    	title = node.find('title')
    	description = node.find('description')
    	link = node.find('link')
    	df_xml = df_xml.append(pd.Series([getvalueofnode(title),getvalueofnode(description),getvalueofnode(link)], index=dfcols),ignore_index=True)
    date_today = date.today()
    df_xml.to_csv("UK news - "+str(date_today)+'.csv')

URL = "https://www.ft.com/world/uk?format=rss"
main(URL)
import datetime
import logging
import requests 
from bs4 import BeautifulSoup
from bs4.element import Comment
import azure.functions as func
#import newsapi
import requests
import json
import os
import uuid


# PowerShell: Set-ExecutionPolicy -ExecutionPolicy Bypass

def main(mytimer: func.TimerRequest, outputTable: func.Out[dict]):
    api_key = '0e218cee2e7c4ae28e2aacdbd69bf977'
    url = 'https://newsapi.org/v2/top-headlines?'

    if mytimer.past_due:
        logging.info('The timer is past due!')


    parameters = {'q': 'corona', 'apiKey': api_key}
    response = requests.get(url, params=parameters)

    top_headlines = response.json() 
    for t in top_headlines["articles"]:
        logging.info(">>>>>>>>>>>>>>>>>> %s (Source: %s)" %(t["title"], t["source"]["name"]))
        rowKey = str(uuid.uuid4())
        outdoc = {
            "title": t["title"], 
            "source": t["source"]["name"],
            "sate": datetime,
            "RowKey": rowKey
        }
        logging.info('Write data to table')
        outputTable.set(outdoc)
        #outputtable.set(t["title"] + " " + t["source"]["name"])


    

    



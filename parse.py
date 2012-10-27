#!/usr/bin/env python
from bs4 import BeautifulSoup
import urllib

url = "http://rubygems.org/gems/"

def get_info(gem):
    web = urllib.urlopen(url + gem)
    data = BeautifulSoup(web)

    depend = {'run': [], 'dev': []}
    depend_run = data.find('div', {'id': 'runtime_dependencies'})
    list = depend_run.find_all('li')
    for value in list:
        depend['run'].append(value.get_text().encode("utf-8").strip().split())

    depend_dev = data.find('div', {'id': 'development_dependencies'})
    list = depend_dev.find_all('li')
    for value in list:
        depend['dev'].append(value.get_text().encode("utf-8").strip().split())

    return depend   

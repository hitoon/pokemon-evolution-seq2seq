# coding:utf-8


"""
# ポケモンデータベース
・ポケモンの日本語名と英語名のセットをスクレイピング
"""

import csv
from bs4 import BeautifulSoup
import requests


url = 'http://pokemon.symphonic-net.com/'

r = requests.get(url)
if r.status_code == requests.codes.ok:

    soup = BeautifulSoup(r.content, 'html.parser')
    trs = soup.findAll("tr")
    result = []
    clm = ['number', 'name', 'type', 'en']
    result.append(clm)
    
    for i in trs[1:]:
        tds = i.findAll('td')
        
        one = []
        for t in tds:
            one.append(t.text)
        try:
            result.append([one[0], one[2], one[3], one[4]])
        except IndexError:
            pass

    print(len(result))

    with open('japanese.csv', 'w') as fw:
        writer = csv.writer(fw, lineterminator='\n')
        writer.writerows(result)

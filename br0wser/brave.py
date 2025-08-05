from bs4 import BeautifulSoup
from lxml import etree
from urllib.parse import quote
import requests

from br0wser.config import *


class Brave:
    def __init__(self):
        self.title = ""
        self.subtitle = ""
        self.text = ""
        self.subtext = ""
        self.ficha = ""
        self.subficha = ""
    
    def searcher(self, pesquisa):
        res = requests.get(f"{browsers.brave_url}{quote(pesquisa)}", headers=headers)
        soup = BeautifulSoup(res.content, "html.parser")
        dom = etree.HTML(str(soup))

        try:
            self.title = dom.xpath('//*[@id="infobox"]/header/div[1]/div/div[1]/a/h1')[0].text
            self.subtitle = dom.xpath('//*[@id="infobox"]//h2')[0].text
            self.text = dom.xpath('//*[@id="infobox"]/header/section/text()')[0]
            self.subtext = dom.xpath('//*[@id="infobox"]/header/section/a')[0].text
            self.ficha = dom.xpath('//*[@id="infobox"]/section[1]/div[2]/header/text()')[0]
            self.subficha = [''.join(div.itertext()).strip() for div in dom.xpath('//*[@id="infobox"]/section[1]/div[2]/div')]
        except:
            return False
        return True
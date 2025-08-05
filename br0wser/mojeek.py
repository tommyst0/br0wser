from bs4 import BeautifulSoup
from lxml import etree
from urllib.parse import quote
import requests

from br0wser.config import *


class Mojeek:
    def __init__(self):
        self.title = ""
        self.subtitle = ""
        self.text = ""
    
    def searcher(self, pesquisa):
        res = requests.get(f"{browsers.mojeek_url}{quote(pesquisa)}", headers=headers)
        soup = BeautifulSoup(res.content, "html.parser")
        dom = etree.HTML(str(soup))

        try:
            self.title = dom.xpath('/html/body/div[1]/div[3]/div[3]/div[2]/h1')[0].text
            self.subtitle = dom.xpath('/html/body/div[1]/div[3]/div[2]/div[1]/div/p[1]')[0].text
            self.text = dom.xpath('/html/body/div[1]/div[3]/div[2]/div[1]/div/p[2]')[0].text
        except:
            return False
        return True
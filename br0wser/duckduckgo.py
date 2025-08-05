from bs4 import BeautifulSoup
from lxml import etree
from urllib.parse import quote
import requests

from br0wser.config import *


class DuckDuckGo:
    def searcher_links(self, query, max_links=10):
        response = requests.post(f"{browsers.duckduckgo_url}{query}", headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            links = []

            for a in soup.find_all("a", class_="result__a", href=True):
                href = a['href']
                links.append(href)
                if len(links) >= max_links:
                    break
            return links      
        else:
            return []  
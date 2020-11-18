
import requests
from enum import Enum
from bs4 import BeautifulSoup

def course_tile_a(tag):
    return tag.name == "a" and tag.has_attr("class") and "product-name" in tag["class"]


class Twoj_Browar_Parser:

    PAGE_URL = "https://twojbrowar.pl/pl/chmiele"

    def __init__(self):
        self.parsed_page = None
        self.last_hop_index = 0
        self.found_hops = []

    def load_page(self):
        response = requests.get(self.PAGE_URL)
        response.raise_for_status()
        self.parsed_page = BeautifulSoup(response.text, features="html.parser")
        return response.status_code
    def parsed_hops(self):
        all_parsed_hops = self.parsed_page.find_all(course_tile_a)
        return all_parsed_hops





parser = Twoj_Browar_Parser()
print(parser.load_page())
print(parser.parsed_hops())

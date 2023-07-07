
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

class Scrpping:
    browser = None

    def __init__(self):
        bravePath = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
        options = webdriver.ChromeOptions()
        options.binary_location = bravePath
        options.page_load_strategy = 'normal'
        self.browser =  webdriver.Chrome(options=options)

    def get_anime_list(self):
        self.browser.get("https://jkanime.net")
        anime_list = self.browser.find_elements(by=By.CLASS_NAME, value='anime__sidebar__comment__item__text')
        self.get_episodie_number('Final')
        recent_anime_list = list(filter(lambda anime: self.is_recent(anime), anime_list))
        parsed_anime_list = list(map(lambda anime: self.parse_anime(anime), recent_anime_list))
        return parsed_anime_list


    def is_recent(self,anime):
        anime_text = anime.text
        print(anime_text)
        return ('Hoy' in anime_text) or ('Ayer' in anime_text)
    
    def parse_anime(self, anime):
        split_anime = anime.text.split('\n')
        anime_dictonary = {
            'anime': split_anime[0],
            'episodie': self.get_episodie_number(split_anime[1]),
        }
        return anime_dictonary
    
    def get_episodie_number(self, episodie_text):
       number =  re.search(r'\d+', episodie_text)
       if number:
        return int(number.group())
       return -1


import re
from selenium import webdriver
from selenium.webdriver.common.by import By
import webbrowser
import subprocess

class Scrpping:
    driver = None
    bravePath = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.binary_location = self.bravePath
        options.page_load_strategy = 'eager'
        self.driver =  webdriver.Chrome(options=options)

    def get_anime_list(self):
        self.driver.get("https://jkanime.net")
        anime_list_container = self.driver.find_element(by=By.CLASS_NAME, value='anime_programing')
        anime_list = anime_list_container.find_elements(by= By.CLASS_NAME, value='bloqq')
        recent_anime_list = list(filter(lambda anime: self.is_recent(anime), anime_list))
        parsed_anime_list = list(map(lambda anime: self.parse_anime(anime), recent_anime_list))
        self.driver.quit()
        return parsed_anime_list


    def is_recent(self,anime):
        anime_text = anime.text
        return ('Hoy' in anime_text) or ('Ayer' in anime_text)
    
    def parse_anime(self, anime):
        split_anime = anime.text.split('\n')
        anime_dictonary = {
            'anime': split_anime[0],
            'episodie': self.get_episodie_number(split_anime[1]),
            'url': anime.get_attribute('href')
        }
        return anime_dictonary
    
    def get_episodie_number(self, episodie_text):
       number =  re.search(r'\d+', episodie_text)
       if number:
        return int(number.group())
       return -1
    
    def open_anime_tabs(self, anime_list):
       first_anime = anime_list.pop()
       self.open_browser(first_anime['url'])
       browser = self.get_browser()
       for anime in anime_list:
          browser.open_new_tab(anime['url'])
    
    def open_browser(self, url):
        subprocess.Popen([self.bravePath, url])

    def get_browser(self):
        webbrowser.register('brave', None, webbrowser.BackgroundBrowser(self.bravePath))
        return webbrowser.get('brave')    

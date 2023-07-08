from src.notion import Notion
from src.scraping import Scrpping

scrap = Scrpping()
ntn = Notion()
anime_jk = scrap.get_anime_list()
scrap.open_anime_tabs(anime_jk)
# animes_notion = ntn.get_data()
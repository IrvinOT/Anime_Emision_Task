from src.notion import Notion
from src.scraping import Scrapping
from src.filter import Filter


scrap = Scrapping()
ntn = Notion()

animes_flv = scrap.get_anime_flv_list()
animes_jk = scrap.get_jk_anime_list()
scrap.close()
animes_notion = ntn.get_data()
filter = Filter(animes_notion, animes_jk, animes_flv)
animes_to_show = filter.get_animes_to_show()
if len(animes_to_show)  == 0:
    exit()
scrap.open_anime_tabs(animes_to_show)
ntn.update_animes(animes_to_show)




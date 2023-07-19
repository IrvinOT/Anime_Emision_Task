class Filter:
    animes_jk = None
    animes_notion = None

    def __init__(self, notion, jk):
        self.animes_notion = notion
        self.animes_jk = jk
    
    def get_animes_to_show(self):
        anime_names = list(map(lambda anime: anime['Name'], self.animes_notion))
        anime_in_jk = list(filter(lambda anime: anime['name'] in anime_names, self.animes_jk))
        
        animes_to_show = list( anime_notion for anime in anime_in_jk if(anime_notion := self.set_anime_notion(anime)) is not None)
        return animes_to_show
    
    def set_anime_notion(self, anime):
        anime_notion = self.get_anime_notioon(anime)
        if anime_notion == None or anime_notion['Episode']['number'] == anime['episodie']:
            return
        
        anime_notion['currentEpisodie'] = anime['episodie']
        anime_notion['url'] = anime['url']
        return anime_notion

    def get_anime_notioon(self, anime):
        name = anime['name']
        return next(filter(lambda row: row['Name'] == name, self.animes_notion), None)
import os
from notion_client import Client
class Notion:
    notion = Client(auth=os.getenv("NOTION_TOKEN"))

    def get_data(self):
        data =self.notion.databases.query(
        **{
            "database_id": os.getenv("DB_NOTION"),
            "filter": {
                "property": "Status",
                "select": {
                    "equals": "emission",
                },
            },
        }
        )
        animes = list(map(self.parse_data, data['results']))
        return animes
    
    def parse_data(self, anime):
        properties = anime['properties']
        parsed = {
            'id': anime['id'],
            'Episode': properties['Episode'],
            'Status': properties['Status'],
            'Name': properties['Name']['title'][0]['plain_text']
        }
        return parsed
    
    def update_animes(self, animes):
        [self.update_anime(anime) for anime in animes]
            

    def update_anime(self, anime):
        end_status = {
            'id':'Dwhm',
            'name':'end',
            'color':'red'
            }
        episode =  anime['currentEpisodie']
        if episode < 0:
            episode = anime['Episode']['number'] + 1
            anime['Status']['select'] = end_status
        
        anime['Episode']['number'] = episode
        data = {
                  'Episode': anime['Episode'],
                  'Status': anime['Status']
            }
        self.notion.pages.update(anime['id'], properties=data)
        


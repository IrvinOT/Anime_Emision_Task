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
        return data['results']


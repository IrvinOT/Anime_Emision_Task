import os
from notion_client import Client

notion = Client(auth=os.environ["NOTION_TOKEN"])

def get_data():
    data =notion.databases.query(
    **{
        "database_id": os.environ["DB_NOTION"],
        "filter": {
            "property": "Status",
            "select": {
                "equals": "emission",
            },
        },
    }
    )
    return data['results']


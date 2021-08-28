import os
import requests


NOTION_KEY = os.getenv("NOTION_KEY")
DATABASE_ID = os.getenv("DATABASE_ID")


def get_database(id: str):
    headers = {
        "Authorization": NOTION_KEY, 
        "Notion-Version": "2021-08-16" 
    }
    url = "https://api.notion.com/v1/databases/" + id

    return requests.get(url, headers=headers)


def get_database_pages(id: str):
    headers = {
        "Authorization": NOTION_KEY, 
        "Notion-Version": "2021-08-16" 
    }
    url = "https://api.notion.com/v1/databases/" + id + "/query"

    return requests.post(url, headers=headers)


if __name__ == "__main__":
    response = get_database_pages(DATABASE_ID)
    print(response.text)

    print(response.text, file=open("test.json", "w"))

    # for item in response["results"]:
    #     content = item["properties"]["Name"]["title"][0]["text"]["content"]
    #     print(content)

    # with open("src/database.json", "r") as f:
    #     data = json.load(f)
    #     for item in data["results"]:
    #         content = item["properties"]["Name"]["title"][0]["text"]["content"]
    #         print(content)

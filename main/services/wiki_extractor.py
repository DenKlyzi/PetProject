import requests

from main import settings

class WikiExtractorService:
    def __init__(self, api_key: str, graphql_url=settings.GRAPHQL_URL):
        self.graphql_url = graphql_url
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

    def get_pages_list(self):
        query = {"query": "{ pages { list { id path title updatedAt } } }"}
        resp = requests.post(self.graphql_url, headers=self.headers, json=query)
        resp.raise_for_status()
        return resp.json()["data"]["pages"]["list"]

    def get_page_content(self, path):
        query = {
            "query": f"""{{
                pages {{
                    singleByPath(path: "{path}") {{
                        content
                    }}
                }}
            }}"""
        }
        resp = requests.post(self.graphql_url, headers=self.headers, json=query)
        resp.raise_for_status()
        data = resp.json()["data"]["pages"]["singleByPath"]
        return data["content"] if data else ""

    def collect_all(self):
        pages = self.get_pages_list()
        dataset = []
        for p in pages:
            content = self.get_page_content(p["path"])
            dataset.append({
                "id": str(p["id"]),
                "text": f"{p['title']}\n{content}",
                "metadata": {
                    "title": p["title"],
                    "path": p["path"],
                    "updatedAt": p["updatedAt"]
                }
            })
        return dataset

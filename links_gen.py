import requests

def get_rand_links(n=2):
    URL = "https://en.wikipedia.org/w/api.php"

    PARAMS = {
        "action": "query",
        "format": "json",
        "list": "random",
        "rnlimit": n,  # Number of random articles to fetch
        "rnnamespace": 0,  # Namespace 0 ensures we're only fetching articlesvv
    }

    response = requests.get(url=URL, params=PARAMS)

    response.raise_for_status()

    data = response.json()

    links = [
        f"https://en.wikipedia.org/wiki/{page['title'].replace(' ', '_')}"
        for page in data["query"]["random"]
    ]
    return links

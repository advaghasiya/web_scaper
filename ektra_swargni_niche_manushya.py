
import requests
from bs4 import BeautifulSoup


def scrape(url):
    """Scrapes the text from a given url"""
    r = requests.get(url)
    r.raise_for_status()
    return r.text

## fetch data from the tag <div class="Poem2-Ekatra"><p>..data...</p></div> 
def fetch_poems(url):
    """Fetches the poems from the given url"""
    soup = BeautifulSoup(scrape(url), "html.parser")
    poems = soup.select("div.Poem2-Ekatra > p")
    return poems


if __name__ == "__main__":
    first = "૧"
    last = "૯"
    for idx, i in enumerate(range(ord(first), ord(last)+1)):
        url = "https://wiki.ekatrafoundation.org/wiki/%E0%AA%B8%E0%AB%8D%E0%AA%B5%E0%AA%B0%E0%AB%8D%E0%AA%97%E0%AA%A8%E0%AB%80_%E0%AA%A8%E0%AB%80%E0%AA%9A%E0%AB%87_%E0%AA%AE%E0%AA%A8%E0%AB%81%E0%AA%B7%E0%AB%8D%E0%AA%AF/%E0%AA%85%E0%AA%A8%E0%AB%81%E0%AA%95%E0%AB%8D%E0%AA%B0%E0%AA%AE/" + chr(i)
        poems = fetch_poems(url)
        with open("book"+str(idx)+".txt", "a", encoding="utf-8") as f:
            for poem in poems:
                f.write(poem.text)
                f.write("\n\n")


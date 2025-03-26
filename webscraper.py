import requests
from bs4 import BeautifulSoup

def scrape_website_links(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'lxml')
        
        links = [a['href'] for a in soup.find_all('a', href=True)]
        
        return links
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []

if __name__ == "__main__":
    url = "https://example.com"
    links = scrape_website_links(url)
    print("Extracted Links:", links)o

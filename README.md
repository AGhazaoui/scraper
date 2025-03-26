# Web Scraper

A simple Python web scraper that extracts links from a given website using `requests` and `BeautifulSoup`.

## Features
- Fetches HTML content from a URL
- Parses the HTML using BeautifulSoup
- Extracts all hyperlinks from the page

## Installation

1. Clone the repository:
   ```sh
   git clone <REPOSITORY>
   cd webscraper
   ```

2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

Run the script with:
```sh
python webscraper.py
```

By default, it scrapes `https://example.com`. Modify the `url` variable in `webscraper.py` to change the target website.

## Requirements
- Python 3.x
- `requests`
- `beautifulsoup4`
- `lxml`

## License
This project is licensed under the MIT License.


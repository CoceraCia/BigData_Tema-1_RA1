# Books Scraper

Web scraping of http://books.toscrape.com/ using requests and BeautifulSoup.
It gets the title and price of every book on the main page.

## Output
- Prints the books on the terminal
- `books.csv` -> title and price of each book
- `inserts.sql` -> INSERT statements ready to use in the SQL exercise

## Run it
```bash
pip install requests beautifulsoup4
python main.py
```

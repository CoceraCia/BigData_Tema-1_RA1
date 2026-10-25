# EJERCICIO 5: Desarrolla un script en Python que realice web scraping de una tienda de libros en
# línea. Extrae el título y el precio de cada libro listado en la página principal de
# http://books.toscrape.com/ usando requests y BeautifulSoup.

import csv
import requests
from bs4 import BeautifulSoup

URL = "http://books.toscrape.com/"


def main():
    books = scrapBooks(URL)

    print("----------- BOOKS -----------")
    for i, book in enumerate(books, start=1):
        print(f"{i}. {book['title']} -> £{book['price']}")
    print(f"Total books: {len(books)}")
    print("-----------------------------")

    # los guardo para usarlos en el ejercicio 6
    saveCSV(books, "books.csv")
    saveInserts(books, "inserts.sql")


def scrapBooks(url: str) -> list[dict]:
    response = requests.get(url)
    response.encoding = "utf-8"  # si no, el simbolo de la libra sale mal (Â£)
    soup = BeautifulSoup(response.text, "html.parser")

    books = []
    # cada libro esta dentro de un <article class="product_pod">
    for article in soup.find_all("article", class_="product_pod"):
        # el titulo completo esta en el atributo title del <a>, el texto viene recortado
        title = article.h3.a["title"]
        price = article.find("p", class_="price_color").text
        books.append({
            "title": title,
            "price": float(price.replace("£", ""))
        })
    return books


def saveCSV(books: list[dict], fileName: str):
    with open(fileName, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "price"])
        writer.writeheader()
        writer.writerows(books)
    print(f"Saved in {fileName}")


def saveInserts(books: list[dict], fileName: str):
    with open(fileName, "w", encoding="utf-8") as f:
        for book in books:
            title = book["title"].replace("'", "''")  # escapar comillas simples para SQL
            f.write(f"INSERT INTO books (title, price) VALUES ('{title}', {book['price']});\n")
    print(f"Saved in {fileName}")


if __name__ == "__main__":
    main()

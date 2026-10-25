-- EJERCICIO 6: Base de datos de libros con los datos del web scraping (ejercicio 5)
-- Compilador: https://www.programiz.com/sql/online-compiler/ (usa SQLite)

-- CREACION DE LA TABLA
CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    price DECIMAL(10,2)
);

-- INSERCION DE DATOS (los 20 libros sacados con el script del ejercicio 5)
INSERT INTO books (title, price) VALUES ('A Light in the Attic', 51.77);
INSERT INTO books (title, price) VALUES ('Tipping the Velvet', 53.74);
INSERT INTO books (title, price) VALUES ('Soumission', 50.1);
INSERT INTO books (title, price) VALUES ('Sharp Objects', 47.82);
INSERT INTO books (title, price) VALUES ('Sapiens: A Brief History of Humankind', 54.23);
INSERT INTO books (title, price) VALUES ('The Requiem Red', 22.65);
INSERT INTO books (title, price) VALUES ('The Dirty Little Secrets of Getting Your Dream Job', 33.34);
INSERT INTO books (title, price) VALUES ('The Coming Woman: A Novel Based on the Life of the Infamous Feminist, Victoria Woodhull', 17.93);
INSERT INTO books (title, price) VALUES ('The Boys in the Boat: Nine Americans and Their Epic Quest for Gold at the 1936 Berlin Olympics', 22.6);
INSERT INTO books (title, price) VALUES ('The Black Maria', 52.15);
INSERT INTO books (title, price) VALUES ('Starving Hearts (Triangular Trade Trilogy, #1)', 13.99);
INSERT INTO books (title, price) VALUES ('Shakespeare''s Sonnets', 20.66);
INSERT INTO books (title, price) VALUES ('Set Me Free', 17.46);
INSERT INTO books (title, price) VALUES ('Scott Pilgrim''s Precious Little Life (Scott Pilgrim #1)', 52.29);
INSERT INTO books (title, price) VALUES ('Rip it Up and Start Again', 35.02);
INSERT INTO books (title, price) VALUES ('Our Band Could Be Your Life: Scenes from the American Indie Underground, 1981-1991', 57.25);
INSERT INTO books (title, price) VALUES ('Olio', 23.88);
INSERT INTO books (title, price) VALUES ('Mesaerion: The Best Science Fiction Stories 1800-1849', 37.59);
INSERT INTO books (title, price) VALUES ('Libertarianism for Beginners', 51.33);
INSERT INTO books (title, price) VALUES ('It''s Only the Himalayas', 45.17);

-- a) Todos los libros ordenados por precio de forma descendente
SELECT * FROM books ORDER BY price DESC;

-- b) Precio promedio de todos los libros
SELECT ROUND(AVG(price), 2) AS precio_promedio FROM books;

-- c) El libro mas caro y el mas barato
SELECT 'Mas caro' AS tipo, title, price FROM books WHERE price = (SELECT MAX(price) FROM books)
UNION ALL
SELECT 'Mas barato', title, price FROM books WHERE price = (SELECT MIN(price) FROM books);

-- d) Cuantos libros tienen un precio superior a 50
SELECT COUNT(*) AS libros_mas_de_50 FROM books WHERE price > 50;

-- e) Titulos de los 5 libros mas baratos
SELECT title FROM books ORDER BY price ASC LIMIT 5;

-- f) Precio total de todos los libros
SELECT ROUND(SUM(price), 2) AS precio_total FROM books;

-- CONSULTA AVANZADA: Barato (menor al promedio) o Caro (mayor o igual al promedio)
SELECT title, price,
    CASE
        WHEN price < (SELECT AVG(price) FROM books) THEN 'Barato'
        ELSE 'Caro'
    END AS categoria
FROM books;

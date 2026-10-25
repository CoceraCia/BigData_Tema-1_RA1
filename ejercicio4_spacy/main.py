# EJERCICIO 4: Utiliza la librería SpaCy de Python para cargar un modelo de lenguaje y procesar
# un texto en busca de nombres propios.
# Como parte opcional, podéis hacer pruebas con textos propios o usar textos existentes para
# probar su eficiencia.

import spacy
import time

# modelo pequeño en español -> python -m spacy download es_core_news_sm
nlp = spacy.load("es_core_news_sm")

exampleText = """Soy Miguel Cocera y actualmente estudio la especialización de Big Data en Linkia FP desde Barcelona.
El año pasado terminé el ciclo de Desarrollo de Aplicaciones Multiplataforma (DAM) y estoy realizando ejercicios de Big Data.
Vamos a testear a ver que tal funciona esto."""


def main():
    while True:
        printMenu()
        option = input("Select an option ->")
        match option:
            case "0":
                print("Bye bye!!")
                return
            case "1":
                analyzeText(exampleText)
            case "2":
                text = input("Write your text:\n")
                analyzeText(text)
            case "3":
                path = input("Path of the .txt file ->")
                analyzeFile(path)
            case _:
                print("WRONG OPTION!!")


def printMenu():
    print("------------- MENU -------------")
    print("0-EXIT")
    print("1-Analyze example text")
    print("2-Analyze your own text")
    print("3-Analyze a .txt file")
    print("--------------------------------")


def analyzeText(text: str):
    start = time.time()
    doc = nlp(text)
    end = time.time()

    # entidades que el modelo reconoce como personas (PER)
    people = [ent.text for ent in doc.ents if ent.label_ == "PER"]
    # el resto de entidades (lugares, organizaciones...)
    others = [(ent.text, ent.label_) for ent in doc.ents if ent.label_ != "PER"]
    # tokens marcados como nombre propio (PROPN)
    propn = [token.text for token in doc if token.pos_ == "PROPN"]

    print("\n----------- RESULT -----------")
    print(f"People found ({len(people)}): {', '.join(people)}")
    print("Other entities:")
    for text_ent, label in others:
        print(f"  - {text_ent} -> {label}")
    print(f"Proper nouns (PROPN): {', '.join(propn)}")
    print(f"Time: {(end - start) * 1000:.2f} ms")
    print("------------------------------\n")


def analyzeFile(path: str):
    try:
        with open(path, "r", encoding="utf-8") as f:
            analyzeText(f.read())
    except FileNotFoundError:
        print("FILE NOT FOUND!!")


if __name__ == "__main__":
    main()

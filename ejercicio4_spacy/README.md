# Proper Nouns Finder with spaCy

Small Python script that loads a spaCy language model (Spanish) and looks for proper nouns in a text.

## How it works
- `doc.ents` -> entities found by the model, I keep the `PER` ones (people)
- `token.pos_ == "PROPN"` -> every word tagged as proper noun
- It also shows the other entities (LOC, ORG, MISC) and how long the model takes

## Menu
```
0-EXIT
1-Analyze example text
2-Analyze your own text
3-Analyze a .txt file
```

## Run it
```bash
pip install spacy
python -m spacy download es_core_news_sm
python main.py
```

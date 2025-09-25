# [Kloop Kyrgyz](https://ky.kloop.asia) crawler.

Crawled content is included in the sqlite3 DB.

# Credits:

-   Thanks to [Bektour Iskender](https://twitter.com/bektour), we were allowed to crawl and use Kloop articles.
-   Thanks to [Henriette Brand's awesome tutorial](https://blog.theodo.com/2019/01/data-scraping-scrapy-django-integration/). My previous attempts to couple Django and Scrapy were [ridiculous](https://github.com/kyrgyz-nlp/readthedocs_cleaned_projects_list/). Her article gave me hints on how to organize the project to make it possible to call Scrapy from within Django.

# Notes:

-   This is currently a work in progress (written in ~8 hours or so).
-   There are 30 934 articles crawled from 2011 to 2024 (as of September 8, 2024). Due to network failures some of the articles were not crawled.
-   It took more than 12 hours to crawl the articles, because of the more or less gentle crawler settings (I didn't want to stress kloop's servers):

```
CONCURRENT_REQUESTS = 3
DOWNLOAD_DELAY = 1
```

## Technology

-   Django 4 (for robust admin panel and awesome ORM)
-   Scrapy (for, surprise, scraping)
-   Other usefult libs (see the project's `requirements` file).

## Explore the corpus

Unpack [all_texts.txt.zip](https://github.com/kyrgyz-nlp/kloop-corpus/blob/main/all_texts.txt.zip) and have fun.

## Dev setup prerequisites

We assume you have the following packages are installed in your system:

-   git
-   Python 3.6 or above
-   venv

## Install dependencies and run

-   Clone the project:
    `git clone https://github.com/kyrgyz-nlp/kloop-corpus.git`

-   Go to the project folder:
    `cd kloop-corpus`

-   Create and activate a virtual env (sorry, Windows users, I don't know how you do this on your machine):
    `python -m venv env && source env/bin/activate`

-   Install project dependecies:
    `pip install -r requirements.txt`

-   Run the server:
    `./manage.py runserver`

-   To run the crawler
    `python manage.py crawl`

## Changelog
-   Sep, 08 2024: re-crawled from the beginning to update all_texts.txt.zip because the articles didn't contain valuable metadata.

## TODO

-   [x] Introduce `--start-year=2020` kind of args to the crawler
-   [ ] Extract metadata using NER models or LLM
-   [ ] Remove whitespaces and remove empty articles
-   [ ] Push the current version of the corpus to Hugging Face
-   [ ] Introduce --start-from='2020-04' kind of args to the crawler
-   [ ] Introduce upsert logic: if the article is not in the DB, then crawl and save
-   [ ] Add webpages with basic corpus statistics: `frequency dictionary`, `most frequent n-grams` etc.

## Citing

If you are using this dataset in your work, please cite it.
```bibtex
@misc{kyrgyz-nlp_kloop-corpus,
  author = {{kyrgyz-nlp}},
  title = {Kloop Corpus},
  year = {2024},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/kyrgyz-nlp/kloop-corpus}},
}
```

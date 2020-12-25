# [Kloop Kyrgyz](https://ky.kloop.asia) crawler.
Crawled content is included in the sqlite3 DB.


# Notes:
* This is currently a work in progress (written in ~8 hours or so).
* The spider in use doesn't know if an article has already been crawled. So this is a TODO.
* There are 16 826 articles crawled from 2011 to 2020 (as of December 25, 2020). Due to network failures some of the articles were not crawled.
* It took more than 12 hours to crawl the articles, because of the more or less gentle crawler settings (I didn't want to stress kloop's servers):
```
ONCURRENT_REQUESTS = 3
DOWNLOAD_DELAY = 1
```

## Technology
* Django 3 (for robust admin panel and awesome ORM)
* Scrapy (for, surprise, scraping)
* Other minor but usefult utils (see the project's `Pipfile`).


## Prerequisites
We assume you have the following packages are installed in your system:
* git
* Python 3.6 or above
* Pipenv


## Install dependencies and run
* Clone the project:
`git clone https://github.com/kyrgyz-nlp/kloop-corpus.git`


* Go to the project folder:
`cd kloop-corpus`


* Install project dependecies:
`pipenv install`


* Activate the project's virtual environment:
`pipenv shell`


* Run the crawler:
`python manage.py crawl`


## TODO
- [ ] Introduce upsert logic: if the article is not in the DB, then crawl and save
- [ ] Remove extra whitespaces from the articles
- [ ] Add webpages with basic corpus statistics: `frequensy dictionary`, `most frequent n-grams` etc.

# [Kloop Kyrgyz](https://ky.kloop.asia) crawler.
Crawled content is included in the sqlite3 DB.


# Credits:
* Thanks to [Bektour Iskender](https://twitter.com/bektour), we were allowed to crawl and use Kloop articles.
* Thanks to [Henriette Brand's awesome](https://blog.theodo.com/2019/01/data-scraping-scrapy-django-integration/). My previous attempts to couple Django and Scrapy were [ridiculous](https://github.com/kyrgyz-nlp/readthedocs_cleaned_projects_list/). Her article gave me hints on how to organize the project to make it possible to call Scrapy from within Django.

# Notes:
* This is currently a work in progress (written in ~8 hours or so).
* The spider in use doesn't know if an article has already been crawled. So this is a TODO.
* There are 16 826 articles crawled from 2011 to 2020 (as of December 25, 2020). Due to network failures some of the articles were not crawled.
* It took more than 12 hours to crawl the articles, because of the more or less gentle crawler settings (I didn't want to stress kloop's servers):
```
CONCURRENT_REQUESTS = 3
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


* Run the server:
`./manage.py runserver`


* Open the following URL to view the articles in the admin panel (username: `admin`, password: `123`):
`http://localhost:8000/admin`


* To run the crawler (Note: the DB already contains Kloops articles):
`python manage.py crawl`


## TODO
- [ ] Introduce upsert logic: if the article is not in the DB, then crawl and save
- [ ] Remove extra whitespaces from the articles
- [ ] Add webpages with basic corpus statistics: `frequensy dictionary`, `most frequent n-grams` etc.

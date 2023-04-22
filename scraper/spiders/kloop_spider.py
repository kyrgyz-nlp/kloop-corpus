import os
import scrapy
import django
from datetime import datetime
from w3lib.html import remove_tags

# Make it possible to run the spider from the project root
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from scraper.spiders.helpers import parse_article
from articles.models import Article


class KloopSpider(scrapy.Spider):
    name = 'kloop'
    start_urls = []

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        current_year = datetime.now().year
        start_year = kwargs.get('start_year') or 2011
        end_year = kwargs.get('end_year') or current_year + 1
        self.start_urls = [
            f'http://ky.kloop.asia/{year}/'
            for year in range(start_year, end_year)
        ]

    def parse(self, response):
        articles_links = response.xpath('//h3/a/@href').getall()
        valid_links = []
        # Check if the links are not already in the database
        for link in articles_links:
            try:
                Article.objects.get(article_url=link)
                log_msg = f'Article {link} already exists in the database'
                self.logger.info(log_msg)
            except Article.DoesNotExist:
                valid_links.append(link)
        yield from response.follow_all(valid_links, self.parse_article)

        next_page_url = response.xpath(
            '//div[@class="page-nav td-pb-padding-side"]/a[last()]/@href'
        ).get()
        if next_page_url:
            yield response.follow(next_page_url, self.parse)

    def parse_article(self, response):
        yield from parse_article(response)

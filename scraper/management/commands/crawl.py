from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from scraper.spiders.kloop_spider import KloopSpider


class Command(BaseCommand):
    help = "Release spiders to crawl articles from 2011 to 2020"

    def handle(self, *args, **options):
        process = CrawlerProcess(get_project_settings())

        process.crawl(KloopSpider)
        process.start()

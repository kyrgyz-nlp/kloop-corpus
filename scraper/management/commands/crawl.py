from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from scraper.spiders.kloop_spider import KloopSpider


class Command(BaseCommand):
    help = "Release spiders to crawl articles from 2011 to 2020"

    def add_arguments(self, parser):
        parser.add_argument('--start-year', type=int)
        parser.add_argument('--end-year', type=int)

    def handle(self, *args, **options):
        start_year = options.get('start_year') or 2011
        end_year = options.get('end_year') or 2024
        process = CrawlerProcess(get_project_settings())

        process.crawl(KloopSpider, start_year=start_year, end_year=end_year)
        process.start()

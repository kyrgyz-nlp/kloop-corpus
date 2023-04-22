from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from scraper.spiders.kloop_features import KloopFeaturesSpider


class Command(BaseCommand):
    help = "Release spiders to crawl feature articles"

    def handle(self, *args, **options):
        process = CrawlerProcess(get_project_settings())

        process.crawl(KloopFeaturesSpider)
        process.start()

import os
import django
import scrapy
from scrapy_playwright.page import PageMethod
from scrapy.selector import Selector

# Make it possible to run the spider from the project root
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from articles.models import Article
from scraper.spiders.helpers import parse_article

LOAD_MORE_TEXT = 'Көбүрөөк жүктө'
LOAD_MORE_SELECTOR = f'a:has-text("{LOAD_MORE_TEXT}")'


class KloopFeaturesSpider(scrapy.Spider):
    name = 'kloop_features'
    allowed_domains = ['ky.kloop.asia']
    start_urls = ['https://ky.kloop.asia/features/']
    custom_settings = {
        "TWISTED_REACTOR": "twisted.internet.asyncioreactor.AsyncioSelectorReactor",
        "DOWNLOAD_HANDLERS": {
            "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
            "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
        },
        "CONCURRENT_REQUESTS": 3,
        "ROBOTSTXT_OBEY": False,
        "DOWNLOAD_DELAY": 1
    }

    def start_requests(self):
        yield scrapy.Request(
            url=self.start_urls[0],
            meta={
                "playwright": True,
                "playwright_page_methods": [
                    PageMethod("wait_for_selector", LOAD_MORE_SELECTOR)
                ],
                "playwright_include_page": True
            },
            errback=self.close_page
        )

    async def parse(self, response):
        page = response.meta['playwright_page']
        while True:
            try:
                await page.get_by_text(LOAD_MORE_TEXT).click()
            except Exception as e:
                print(e)
                break
        page_content  = Selector(text=await page.content())
        await page.close()
        for link in page_content.css('h3 a::attr(href)').getall():
            try:
                await Article.objects.aget(article_url=link)
                log_msg = f'Article {link} already exists in the database'
                self.logger.info(log_msg)
            except Article.DoesNotExist:
                yield scrapy.Request(
                    url=link,
                    callback=self.parse_article,
                    errback=self.close_page
                )

    def parse_article(self, response):
        yield from parse_article(response)

    async def close_page(self, failure):
        page = failure.request.meta["playwright_page"]
        await page.close()
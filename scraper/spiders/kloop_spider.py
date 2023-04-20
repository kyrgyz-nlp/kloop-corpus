import re
import scrapy
import dateparser

from w3lib.html import remove_tags

from articles.models import Article
from scraper.items import ArticleItem


SCRIPT_TAGS_PATTERN = r'<[ ]*script.*?\/[ ]*script[ ]*>'


def _remove_js(text):
    text_w_script_tag = remove_tags(text, keep=('script',))
    clean = re.sub(
        SCRIPT_TAGS_PATTERN, '', text_w_script_tag,
        flags=(re.IGNORECASE | re.MULTILINE | re.DOTALL))
    return clean


class KloopSpider(scrapy.Spider):
    name = 'kloop'
    start_urls = []


    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        start_year = kwargs.get('start_year')
        end_year = kwargs.get('end_year')
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
        url = response.url
        title = response.xpath('//h1[@class="entry-title"]').get()
        text = response.xpath('//div[@class="td-post-content"]').get()
        posted_by = response.xpath(
            '//div[@class="td-post-author-name"]/a').get()
        dt_xpath = (
            '//article//div[@class="td-module-meta-info"]/'
            'span[@class="td-post-date"]/'
            'time[@class="entry-date updated td-module-date"]/@datetime'
        )
        post_date = response.xpath(dt_xpath).get()
        created_at = dateparser.parse(post_date)
        item = ArticleItem()
        item['title'] = remove_tags(title)
        item['text'] = _remove_js(text)
        item['article_url'] = url
        item['created_at'] = created_at
        item['posted_by'] = remove_tags(posted_by)
        yield item

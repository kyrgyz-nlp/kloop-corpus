import scrapy
import dateparser

from scraper.items import ArticleItem


class KloopSpider(scrapy.Spider):
    name = 'kloop'
    start_urls = [
        f'http://ky.kloop.asia/{year}/' for year in range(2011, 2021)]

    def parse(self, response):
        articles_links = response.xpath('//h3/a/@href').getall()
        yield from response.follow_all(articles_links, self.parse_article)

        pagination_last_link_title = response.xpath(
            '//a[@class="last"]/@title').get()
        if pagination_last_link_title:
            last_page_num = int(pagination_last_link_title)
            pages_range = range(1, last_page_num + 1)
            url_template = 'https://ky.kloop.asia/2011/page/{}/'
            pagination_links = [
                url_template.format(page_num) for page_num in pages_range]
            yield from response.follow_all(pagination_links, self.parse)

    def parse_article(self, response):
        url = response.url
        title = response.xpath('//h1[@class="entry-title"]').get()
        text = response.xpath('//div[@class="td-post-content"]').get()
        posted_by = response.xpath(
            '//div[@class="td-post-author-name"]/a').get()
        dt_xpath = (
            '//span[@class="td-post-date td-post-date-no-dot"]/'
            'time[@class="entry-date updated td-module-date"]/@datetime')
        post_date = response.xpath(dt_xpath).get()
        created_at = dateparser.parse(post_date)
        item = ArticleItem()
        item['title'] = title
        item['text'] = text
        item['article_url'] = url
        item['created_at'] = created_at
        item['posted_by'] = posted_by
        yield item

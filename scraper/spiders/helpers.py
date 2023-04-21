import os
import re
import dateparser
import django
from w3lib.html import remove_tags

# Make it possible to run the spider from the project root
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from scraper.items import ArticleItem


def get_tag_pattern(tag_name):
    res = r'<[ ]*{tag}.*?\/[ ]*{tag}[ ]*>'.format(tag=tag_name)
    return res


def clean_with_regex(text, pattern):
    clean = re.sub(
        pattern, '', text,
        flags=(re.IGNORECASE | re.MULTILINE | re.DOTALL))
    return clean


def remove_js_and_css(text):
    text_w_script_tag = remove_tags(text, keep=('script','style'))
    script_tag_pattern = get_tag_pattern('script')
    style_tag_pattern = get_tag_pattern('style')
    clean = clean_with_regex(text_w_script_tag, script_tag_pattern)
    clean = clean_with_regex(clean, style_tag_pattern)
    return clean


def parse_article(response):
    url = response.url
    title = response.xpath('//h1[@class="entry-title"]').get()
    text = response.xpath('//div[contains(@class, "td-post-content")]').get()
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
    item['text'] = remove_js_and_css(text)
    item['article_url'] = url
    item['created_at'] = created_at
    item['posted_by'] = remove_tags(posted_by)
    yield item

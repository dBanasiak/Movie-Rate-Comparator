from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

URL_QUERY = (
    'https://www.imdb.com/search/title?'
    'title_type=feature&'
    'user_rating=1.0,10.0&'
    'release_date='
    'countries=us&'
    'languages=en&'
    'count=250'
)

class ImdbSpider(CrawlSpider):
    name = 'movie'
    allowed_domains = ['https://www.imdb.com/']
    start_urls = [URL_QUERY]


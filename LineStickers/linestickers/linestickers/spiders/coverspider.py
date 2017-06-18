# Import the necessary packages
from linestickers.items import LinestickersItem
import scrapy
import re

class CoverSpider(scrapy.Spider):
    name = "line-sticker-cover-spider"

    def __init__(self, *args, **kwargs):
        super(CoverSpider,self).__init__(*args, **kwargs)
        self.start_urls = [kwargs.get('start_url')]

    def parse(self, response):
        urlreg = r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)'
        urlRegex = re.compile(urlreg)
        img_map = dict()
        line_stickers = LinestickersItem()

        line_stickers['name'] = response.css('h3::text').extract_first()
        line_stickers['file_urls'] = []

        for img_style in response.css('.mdCMN09Image::attr(style)').extract():
            search_obj = urlRegex.search(img_style)
            img_url = search_obj.group()
            line_stickers['file_urls'].append(img_url)

        yield line_stickers










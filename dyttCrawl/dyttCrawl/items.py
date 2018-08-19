# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from thunder.models import DyttItem
from scrapy_djangoitem import DjangoItem
import scrapy

class DyttcrawlItem(DjangoItem):
    django_model = DyttItem
    pass

# class DyttcrawlItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass

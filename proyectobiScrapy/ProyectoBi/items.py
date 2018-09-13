# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProyectobiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    #informacion del producto
    titulo = scrapy.Field()
    tipo = scrapy.Field()
    precio = scrapy.Field()
    condicion = scrapy.Field()
    ubicacion = scrapy.Field()
    tiempo = scrapy.Field()
    pago = scrapy.Field()
    #info de la tiendo o vendedor
    reputacion = scrapy.Field()

    pass

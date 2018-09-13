# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ProyectoBi.items import ProyectobiItem

class ProyectoBISPider(CrawlSpider):

    name = 'proyectobi'
    item_count = 0
    allowed_domain = ['www.mercadolibre.com.ec']
    start_urls = ['https://listado.mercadolibre.com.ec/relojes_DisplayType_LF#D[A:relojes]']

    rules = {
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//*[@id="results-section"]/div[2]/ul/li[12]/a'))),
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//h2[contains(@class,"item__title")]/a')),
                                     callback = 'parse_item', follow= False)
    }

    def parse_item(self, response):
        ml_item  = ProyectobiItem()

        #info de producto
        ml_item['titulo'] = response.xpath('normalize-space(//*[@id="short-desc"]/div/header/h1/text())').extract_first()
        ml_item['tipo'] = response.xpath('normalize-space(/html/body/main/section[1]/nav/div[1]/ul/li[2]/a/text())').extract()
        ml_item['precio'] = response.xpath('normalize-space(//span[@class ="price-tag-fraction"]/text())').extract()
        ml_item['condicion'] = response.xpath('normalize-space(//div[@class = "item-conditions"]/text())').extract()
        ml_item['ubicacion'] = response.xpath('normalize-space(//p[@class ="custom-address"])').extract()
        ml_item['tiempo'] = response.xpath('normalize-space(//strong[@class ="history-data"]/text())').extract()
        ml_item['pago'] = response.xpath('normalize-space(//p[@class = "text-light"])').extract()

        #info de la tiendo o vendedor
        ml_item['reputacion'] = response.xpath('normalize-space(/html/body/main/div/div[1]/div[2]/div[1]/section[2]/div[3]/div/div/div/dl/dd[1])').extract()

        self.item_count += 1

        if self.item_count > 100:
            raise CloseSpider('item_exceeded')
        yield ml_item


#https://listado.mercadolibre.com.ec/licuadoras_DisplayType_LF#D[A:licuadoras]
#https://listado.mercadolibre.com.ec/computadoras_DisplayType_LF#D[A:computadoras]
#https://listado.mercadolibre.com.ec/impresoras_DisplayType_LF#D[A:impresoras]
#https://listado.mercadolibre.com.ec/relojes_DisplayType_LF#D[A:relojes]
#https://listado.mercadolibre.com.ec/televisores_DisplayType_LF#D[A:televisores]

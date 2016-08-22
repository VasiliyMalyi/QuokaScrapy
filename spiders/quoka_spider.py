import scrapy
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from TaskSolve.items import TasksolveItem
from datetime import datetime


class QuokaSpider(CrawlSpider):
    name = 'quoka'
    allowed_domains = ["quoka.de"]
    start_urls = [
        'http://www.quoka.de/qmca/search/search.html?redirect=0&catid=27_2710&pageNo=%d' % page for page in range(280)
    ] # Creating list of urls. For 280 pages for now, but would be better to know exactly how many
    
    rules = (
        Rule(LinkExtractor(allow=('c2710')), callback='parse_item'),
        )

    def parse_item(self, response):
        sels = Selector(response).xpath("//*")
        for sel in sels:
            item = TasksolveItem()
            item['Boersen_ID'] = ''
            item['OBID'] = sel.xpath('/html/body/div[3]/div[2]/div[1]/main/div[4]/div/div[3]/div[2]/div[2]/strong[1]/text()').extract()[0]
            item['erzeugt_am'] = datetime.now()
            item['Anbieter_ID'] = ''
            item['Anbieter_ObjektID'] = ''
            item['Immobilientyp'] = 'Buros,Gewerbeflachen'
            item['Immobilientyp_detail'] = ''
            item['Vermarktungstyp'] = 'kaufen'
            item['Land'] = 'Deutschland'
            item['Bundesland'] = ''
            item['Bezirk'] = ''
            item['Stadt'] = sel.xpath('/html/body/div[3]/div[2]/div[1]/main/div[4]/div/div[3]/div[2]/div[1]/strong/span/span/span[1]/text()').extract()[0]
            item['PLZ'] = sel.xpath("/html/body/div[3]/div[2]/div[1]/main/div[4]/div/div[3]/div[2]/div[1]/strong/span/span/span[2]/text()").extract()[0]
            item['Strasse'] = ''
            item['Hausnummer'] = ''
            item['Uberschrift'] = sel.xpath('/html/body/div[3]/div[2]/div[1]/main/div[4]/div/div[1]/h1/text()').extract()[0]
            item['Beschreibung'] = sel.xpath('/html/body/div[3]/div[2]/div[1]/main/div[4]/div/div[3]/div[3]/div/text()').extract()
            item['Etage'] = '' 
            item['Kaufpreis'] = sel.xpath('/html/body/div[3]/div[2]/div[1]/main/div[4]/div/div[2]/strong/span/text()').extract()
            item['Kaltmiete'] = ''
            item['Warmmiete'] = ''
            item['Nebenkosten'] = ''
            item['Zimmeranzahl'] = ''
            item['Wohnflaeche'] = ''
            item['Monat'] = datetime.now().month
            item['url'] = response.url
            item['Telefon'] = sel.xpath('//*[@id="Handy1"]/span/text()').extract()
            item['Erstellungsdatum'] = sel.xpath('/html/body/div[3]/div[2]/div[1]/main/div[4]/div/div[3]/div[2]/div[2]/text()').extract() + sel.xpath('/html/body/div[3]/div[2]/div[1]/main/div[4]/div/div[3]/div[2]/div[2]/span/text()').extract()
            item['Gewerblich'] = 1            

        yield item


       
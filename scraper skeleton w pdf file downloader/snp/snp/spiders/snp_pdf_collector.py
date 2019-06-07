import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from snp.items import SnpItem


class SnpPdfCollectorSpider(scrapy.Spider): #scrapy.Spider
	name = "snp_pdf_collector"
	#allowed_domains = ["www.standardandpoors.com", "www.eu.spindices.com", "www.spice-indices.com"] # "www.standardandpoors.com", "https://eu.spindices.com", "https://www.spice-indices.com/"
	allowed_domains = ["www.standardandpoors.com", "eu.spindices.com"] # "www.standardandpoors.com", "https://eu.spindices.com", "https://www.spice-indices.com/"
	start_urls = ["https://eu.spindices.com/search/?page=1&query=&sortType=Date&resultsPerPage=1000&ContentType=Announcement&AssetFamily=equity&Region=region-americas"]
	rules = (Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),)
	
	def parse_item(self, response):
		i = {}
		return i

	def parse(self, response):
		#pdf_link_base = "https://www.spice-indices.com/idpfiles/spice-assets/resources/public/documents"
		pdf_link_base = 'https://eu.spindices.com/documents/indexnews/announcements/'
		results = response.css('div.result')

		for result in results:

			if ' to Join ' in result.css('h3 > a::text').extract_first():

				title = result.css('h3 > a::text').extract_first()
				src = result.css('h3 > a::attr(href)').extract_first()
				src = src[src.find('/201')+1:][src[src.find('/201')+1:].find('/'):]

				if src.endswith("?force_download=true"):
					src = src[:len("?force_download=true")*-1]

				src = pdf_link_base + src
				
				yield SnpItem(title=title, file_urls=[src])

			else:
				continue
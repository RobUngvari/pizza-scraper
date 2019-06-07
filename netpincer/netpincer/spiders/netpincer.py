import scrapy


class NetpincerSpider(scrapy.Spider):
    name = "netpincer"

    def start_requests(self):
        urls = [
            'https://www.netpincer.hu/hazhozszallitas/budapest_ix'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        for x in response.css('a[class="item clearfix"]'):

            item = {

                "name" : x.css('div[class="name-container"] > h2::text').extract_first(),
                "number": x.css('div[class="rate-container"] > div > b::text').extract_first(),
                "rate": x.css('div[class="rate-container"] > div > span::text').extract_first(),
            }
            yield item
        # yield {
        #
        #     "name" : response.css('div[class="name-container"] > h2::text').extract(),
        #     "number": response.css('div[class="rate-container"] > div > b::text').extract(),
        #     "rate": response.css('div[class="rate-container"] > div > span::text').extract(),
        # }
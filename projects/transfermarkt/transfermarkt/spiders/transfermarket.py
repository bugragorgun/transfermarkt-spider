import scrapy
from scrapy_splash import SplashRequest

class TransfermarketSpider(scrapy.Spider):
    name = 'transfermarket'
    allowed_domains = ['transfermarkt.com']
    start_urls = ['https://www.transfermarkt.com.tr/super-lig/besucherzahlen/wettbewerb/TR1/']
    
    # def start_requests(self):
    #     yield SplashRequest(url="https://www.transfermarkt.com.tr/super-lig/besucherzahlen/wettbewerb/TR1", callback=self.parse, endpoint="execute", args={
    #         'lua_source': self.script
    #     })

    # def start_request(self):
    #     yield scrapy.Request(url='https://www.transfermarkt.com.tr/super-lig/besucherzahlen/wettbewerb/TR1', callback=self.parse, headers={
    #         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    #         })

    def parse(self, response):
        # stadiums = response.xpath("//div[@id='yw1']/table[@class='items']/tbody/tr")
        print(response.body)
        
        for stadium in response.xpath("//div[@id='yw1']/table[@class='items']/tbody/tr"):
            yield{
                'stadium_name':stadium.xpath(".//td[2]/table/tbody/tr/td[2]/a/text()").get(),
                'capacity': stadium.xpath(".//td[3]/text()").get(),
                'audience': stadium.xpath(".//td[4]/text()").get(),
                'average':stadium.xpath(".//td[5]/text()").get()
            }
                    
            # yield{
            #     'stadium_name':name,
            #     'capacity':capacity,
            #     'audience':audience,
            #     'average':average,
            #     'User-Agent': response.request.headers['User-Agent']
            # }



        

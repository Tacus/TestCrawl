import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    custom_settings = {
    "DEFAULT_REQUEST_HEADERS":{
        'User-Agent':'User-Agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Mobile Safari/537.36',
        'x-csrf-token': 'jAu0IDWXDf4Ikjc-8nYltxzo',
        'X-token': '1114160773',
        }

    }
    def start_requests(self):
        urls = [
            'Request URL: https://bugly.qq.com/v2/issueList?start=0&searchType=errorType&exceptionTypeList=AllCatched,Unity3D,Lua,JS&pid=1&platformId=1&sortOrder=desc&version=1.0.62&rows=10&sortField=uploadTime&appId=c57b075caf&fsn=93a34258-8e97-420f-8e40-57ca46824915',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
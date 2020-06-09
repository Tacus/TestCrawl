# -*- coding: utf-8 -*-

# Scrapy settings for tutorial project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'tutorial'

SPIDER_MODULES = ['tutorial.spiders']
NEWSPIDER_MODULE = 'tutorial.spiders'

DEFAULT_REQUEST_HEADERS={
    # "Origin":"http://baidu.com",
	"Accept": "application/json;charset=utf-8",
    "Accept-Language": "zh,zh-CN;q=0.9,en;q=0.8",
    "Accept-Encoding":"gzip, deflate",
    "Connection":"keep-alive",
    "Content-Type":"application/json;charset=utf-8",
    "Cookie":"pgv_pvi=438138880; RK=NYggDNA8Hu; ptcz=1d39a7c8f10147401ff87a11f44ac75b1f2076cbd19e4ca20bf9c949e5b20756; pgv_pvid=8483331616; o_cookie=184624026; pac_uid=1_184624026; tvfe_boss_uuid=e553d159a511b3a4; XWINDEXGREY=0; ptui_loginuin=184624026; _ga=GA1.2.692313245.1585223620; btcu_id=876711e194caa4a523f06ffe6df4c1235e7c97c3b50cd; vc=vc-2b1c9686-70a1-43a4-b11b-ddc97770c207; vc.sig=bN5lHXB1JyTj8Fzz6ehxRxeU478NCEaqjGbomsHs0dc; vc=vc-fe3b695c-a2a4-4909-9f80-8b944cdd6026; btcu_id=0b861290-1233-4c37-b123-99cf87f05c41; gaduid=5e8587bb37849; pgv_si=s3324956672; pgv_info=ssid=s7219466864; _gid=GA1.2.1351980733.1591683200; NODINX_SESS=sIy7SHai6obHJrbhnOXT9c8nZzHtXP8i-ePiYVpbLJiL9WsK1aP6WGLz8LjwBswr; csrfToken=jAu0IDWXDf4Ikjc-8nYltxzo; token-skey=b692c56f-7761-9ce7-8d01-51b5d751271c; token-lifeTime=1591723012; _gat=1; referrer=eyJpdiI6IkJkMXRWOVgyYk45YkEzWHZCeE91TGc9PSIsInZhbHVlIjoiVUZwaEg4U0dTTmV3OENsQTBUVDRrMTdxTkFVVDF4SCtaQit2MzZoTFBPZlNGQ0V6RHhHYU5RU09Ba0tUMEZyek52TzIxT3Y1TmxuTVlKRjZUOEViN0dpTERXV0ZrQUVBVUpDZUxXWTNoeGF5TVRxTmR4MDRJM21wZGVjTDNDUXpqKzM3eUFPakZjSWVcL3dOYlpTTXFIMWxhUFU2bFFGNGI5Y0ZlOFRvd3lcLzA9IiwibWFjIjoiODg3YjIyODQ2OGE0ZjBiMGJkYThiMmYxOWJmZTE4YzUxNjBlOWE3YWVjNTA4YTcxYzFiYWU3YjE1NjM3ZDJmZCJ9; bugly_session=eyJpdiI6IlNSbEJPUk04bGJrXC9sRzlaUG1tajBnPT0iLCJ2YWx1ZSI6IndTSVZ0anZXejBuVkN3a2M4dXE5T0hxb2I3Z2NlSnFweUZ3Zys5VHlPeXY2c01LaWlHcGdEeEFKMm1rQTRJXC9mcFpnZlwvQlJoVXNpdmZoajJpcStuQ0E9PSIsIm1hYyI6ImUwMDI4MzM5YzNiOGQ2MjIyZjViMmMwNmZjNTM0ZDc1MmZhYWYwYmYyYWY1NGI0ZjQ4ZDNmZWYzZDMwODQzMTcifQ%3D%3D",
    "Host":"bugly.qq.com",
    "Referer": "https://bugly.qq.com/v2/crash-reporting/errors/c57b075caf?pid=1&version=1.0.62&start=0",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Mobile Safari/537.36",
    "x-csrf-token": "jAu0IDWXDf4Ikjc-8nYltxzo",
    "X-token": "1389971317"
}


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'tutorial.middlewares.TutorialSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'tutorial.middlewares.TutorialDownloaderMiddleware': 543,
    'tutorial.middlewares.AgentMiddleware': None,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'tutorial.pipelines.TutorialPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

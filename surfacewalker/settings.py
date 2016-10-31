# -*- coding: utf-8 -*-
BOT_NAME = 'testfrontera'

SPIDER_MODULES = ['testfrontera.spiders']
NEWSPIDER_MODULE = 'testfrontera.spiders'

SPIDER_MIDDLEWARES = {
    'frontera.contrib.scrapy.middlewares.schedulers.SchedulerSpiderMiddleware': 1000,
    'frontera.contrib.scrapy.middlewares.seeds.FileSeedLoader': 650
}
DOWNLOADER_MIDDLEWARES = {
    'frontera.contrib.scrapy.middlewares.schedulers.SchedulerDownloaderMiddleware': 1000,
}
SCHEDULER = 'frontera.contrib.scrapy.schedulers.frontier.FronteraScheduler'
FRONTERA_SETTINGS = 'testfrontera.frontera.settings'
SEEDS_SOURCE = 'top500-seed.txt'

HTTPCACHE_ENABLED = False   # Turns off disk cache, which has low hit ratio during broad crawls
REDIRECT_ENABLED = True
COOKIES_ENABLED = False
DOWNLOAD_TIMEOUT = 120
RETRY_ENABLED = False
DOWNLOAD_MAXSIZE = 10 * 1024 * 1024
LOGSTATS_INTERVAL = 10

# auto throttling
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_DEBUG = False
AUTOTHROTTLE_MAX_DELAY = 3.0
AUTOTHROTTLE_START_DELAY = 0.25
RANDOMIZE_DOWNLOAD_DELAY = False
# concurrency
CONCURRENT_REQUESTS = 256
CONCURRENT_REQUESTS_PER_DOMAIN = 10
DOWNLOAD_DELAY = 0.0

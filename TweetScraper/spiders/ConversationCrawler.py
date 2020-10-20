import re
import logging
from urllib.parse import quote

from scrapy import http
from scrapy.exceptions import CloseSpider
from scrapy_selenium import SeleniumRequest, SeleniumMiddleware
from scrapy.core.downloader.middleware import DownloaderMiddlewareManager

from .TweetScraper import TweetScraper

logger = logging.getLogger(__name__)


class ConversationCrawlerSpider(TweetScraper):
    name = 'ConversationCrawler'

    def __init__(self, tweet_id=None):

        if tweet_id is None:
            raise CloseSpider('No tweet id attribute passed')

        self.url = (
            f'https://twitter.com/i/api/2/timeline/conversation/{tweet_id}.json?'
            f'include_profile_interstitial_type=1'
            f'&include_blocking=1'
            f'&include_blocked_by=1'
            f'&include_followed_by=1'
            f'&include_want_retweets=1'
            f'&include_mute_edge=1'
            f'&include_can_dm=1'
            f'&include_can_media_tag=1'
            f'&skip_status=1'
            f'&cards_platform=Web-12'
            f'&include_cards=1'
            f'&include_ext_alt_text=true'
            f'&include_quote_count=true'
            f'&include_reply_count=1'
            f'&tweet_mode=extended'
            f'&include_entities=true'
            f'&include_user_entities=true'
            f'&include_ext_media_color=true'
            f'&include_ext_media_availability=true'
            f'&send_error_codes=true'
            f'&simple_quoted_tweet=true'
            f'&query_source=typed_query'
            f'&pc=1'
            f'&spelling_corrections=1'
            f'&ext=mediaStats%2ChighlightedLabel'
            f'&count=20'
        )
        self.tweet_id = tweet_id
        self.num_search_issued = 0
        # regex for finding next cursor
        self.cursor_re = re.compile(r'"cursor":{"value":"(.+?)"')

    def start_query_request(self, cursor=None):

        if cursor:
            url = self.url + '&cursor={cursor}'
            url = url.format(cursor=quote(cursor))
        else:
            url = self.url
        request = http.Request(url, callback=self.parse_result_page, cookies=self.cookies, headers=self.headers)
        yield request

        self.num_search_issued += 1
        if self.num_search_issued % 100 == 0:
            # get new SeleniumMiddleware
            for m in self.crawler.engine.downloader.middleware.middlewares:
                if isinstance(m, SeleniumMiddleware):
                    m.spider_closed()
            self.crawler.engine.downloader.middleware = DownloaderMiddlewareManager.from_crawler(self.crawler)
            # update cookies
            yield SeleniumRequest(url="https://twitter.com/explore", callback=self.update_cookies, dont_filter=True)

import json
import codecs
from ..Models import Tweet

class TweetFileExtractor:
    @staticmethod
    def handle(filepath, exclude=()):
        with codecs.open(filepath, 'r', 'UTF-8') as file:
            data = json.load(file)
            return Tweet(data['raw_data']['full_text']) if data['raw_data']['user_id_str'] not in exclude else None

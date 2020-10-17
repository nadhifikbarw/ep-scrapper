import json
import codecs
from ..Models import Tweet

class TweetFileExtractor:
    @staticmethod
    def handle(filepath):
        with codecs.open(filepath, 'r', 'UTF-8') as file:
            data = json.load(file)
            return Tweet(data['raw_data']['full_text'])

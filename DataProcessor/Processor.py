from os import walk
from .Loaders import CSVLoader
from os.path import join as pathjoin
from .Extractors import TweetFileExtractor
from .Transformers import HTMLTransformer
from .Transformers import TweetTransformer
from .Transformers import LowercaseTransformer
from .Transformers import WhitespaceTransformer
from .Transformers import PunctuationTransformer


class Processor:
    # Input path
    input_path = ''

    # Output path
    output_path = ''

    # Data
    tweets = []

    # Tweet Path
    tweet_paths = []

    # Transformer handlers
    handlers = [
        HTMLTransformer(),
        LowercaseTransformer(),
        TweetTransformer(),
        PunctuationTransformer(),
        WhitespaceTransformer()
    ]

    loaders = []

    def __init__(self, dir_path, out_path):
        # Prepare path
        self.input_path = dir_path
        self.output_path = out_path

        # Create loader
        self.loaders.append(CSVLoader(self.output_path).open(append=False))

        # Walk input directory
        self.__get_tweet_paths()

    def __get_tweet_paths(self):
        for anchor, directories, files in walk(self.input_path):
            for filename in files:
                self.tweet_paths.append(pathjoin(anchor, filename))

    def __extract(self):
        self.tweets = [TweetFileExtractor.handle(file) for file in self.tweet_paths]

    def __transform(self):
        for tweet in self.tweets:
            for transformer in self.handlers:
                tweet.fulltext = transformer.handle(tweet)

    def __load(self):
        for loader in self.loaders:
            for tweet in self.tweets:
                if tweet.getText() != '':
                    loader.write(tweet)
            loader.close()

    def handle(self):
        self.__extract()
        self.__transform()
        self.__load()

from .Loaders import CSVLoader
from .Extractors import TweetXSLXExtractor
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

    # Transformer handlers
    handlers = [
        HTMLTransformer(),
        LowercaseTransformer(),
        TweetTransformer(),
        PunctuationTransformer(),
        WhitespaceTransformer()
    ]

    loaders = []

    def __init__(self, input_path, out_path):
        # Prepare path
        self.input_path = input_path
        self.output_path = out_path

        # Create loader
        self.loaders.append(CSVLoader(self.output_path).open(append=False))

    def __extract(self):
        self.tweets = TweetXSLXExtractor.handle(self.input_path)

    def __transform(self):
        for tweet in self.tweets:
            for transformer in self.handlers:
                tweet.fulltext = transformer.handle(tweet)

    def __load(self):
        for loader in self.loaders:
            for tweet in self.tweets:
                if tweet.getText() != '' and tweet.getTag() != 'tdkRelevan':
                    loader.write(tweet)
            loader.close()

    def handle(self):
        self.__extract()
        self.__transform()
        self.__load()

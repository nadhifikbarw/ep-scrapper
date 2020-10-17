import preprocessor as p
from ..Models import Tweet
from .Transformer import Transformer


class TweetTransformer(Transformer):

    def __init__(self):
        self.preprocessor = p

    def handle(self, model: Tweet):
        return self.preprocessor.clean(model.getText())

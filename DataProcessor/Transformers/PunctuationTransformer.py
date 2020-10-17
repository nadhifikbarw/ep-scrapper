import string
from ..Models import Tweet
from .Transformer import Transformer


class PunctuationTransformer(Transformer):

    def __init__(self):
        self.translator = str.maketrans(string.punctuation, ' '*len(string.punctuation))

    def handle(self, model: Tweet):
        return model.getText().translate(self.translator)
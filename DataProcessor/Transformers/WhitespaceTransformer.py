from re import sub
from ..Models import Tweet
from .Transformer import Transformer


class WhitespaceTransformer(Transformer):

    def handle(self, model: Tweet):
        return sub(r'\s{2,}', ' ', model.getText()).strip()

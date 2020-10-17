import html
from ..Models import Tweet
from .Transformer import Transformer


class HTMLTransformer(Transformer):

    def handle(self, model: Tweet):
        return html.unescape(model.getText())

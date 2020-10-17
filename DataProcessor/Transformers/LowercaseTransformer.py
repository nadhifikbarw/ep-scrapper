from ..Models import Tweet
from .Transformer import Transformer


class LowercaseTransformer(Transformer):

    def handle(self, model: Tweet):
        return model.getText().lower()

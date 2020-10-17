from .Model import Model


class Tweet(Model):
    fulltext: str = None

    def __init__(self, ft: str):
        self.fulltext: str = ft

    def getText(self) -> str:
        return self.fulltext

from .Model import Model


class Tweet(Model):
    fulltext: str = None

    tag: str = None

    def __init__(self, ft: str, tag=None):
        self.fulltext: str = ft
        self.tag: str = tag

    def getText(self) -> str:
        return self.fulltext

    def getTag(self) -> str:
        return self.tag

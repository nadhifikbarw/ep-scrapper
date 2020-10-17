from ..Models import Model
from .LoaderState import LoaderState


class Loader:

    STATE = LoaderState

    def open(self):
        pass

    def write(self, model: Model):
        pass

    def close(self):
        pass

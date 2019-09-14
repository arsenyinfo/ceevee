import numpy as np

from ceevee.base import AbstractBaseline


class DummyBaseline(AbstractBaseline):
    """
    The model effectively does nothing
    """

    def __init__(self):
        super().__init__()

    def preprocess(self, x, *kw):
        return x

    def process(self, x, *kw):
        return np.array(x.shape)

    def postprocess(self, x, *kw):
        return x

    def __call__(self, x, *args, **kwargs):
        x = self.preprocess(x)
        x = self.process(x)
        x = self.postprocess(x)
        return {'success': True, 'result': x}

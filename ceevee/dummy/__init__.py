import numpy as np

from ceevee.base import AbstractPredictor


class DummyPredictor(AbstractPredictor):
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

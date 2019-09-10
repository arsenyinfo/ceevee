import abc

import numpy as np
import torch


class AbstractBaseline:
    @abc.abstractmethod
    def __init__(self):
        pass

    def __call__(self, x, *args, **kwargs) -> dict:
        assert len(x.shape) == 3, "Batch mode is not supported for a while"
        h, w, _ = x.shape
        x = self.preprocess(x)
        res = self.process(x)
        res = self.postprocess(res)
        return res

    @abc.abstractmethod
    def preprocess(self, x, *kw):
        pass

    @abc.abstractmethod
    def process(self, x, *kw):
        pass

    @abc.abstractmethod
    def postprocess(self, x, *kw):
        pass

    @staticmethod
    def _array_to_batch(x):
        x = np.transpose(x, (2, 0, 1))
        x = np.expand_dims(x, 0)
        return torch.from_numpy(x)

    @staticmethod
    def _batch_to_array(x):
        assert x.size()[0] == 1, "Batch size = 1 is only supported for a while"
        x, = x.cpu().numpy()
        x = np.transpose(x, (1, 2, 0))
        return x


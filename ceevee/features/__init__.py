from functools import partial

import cv2
import numpy as np
import torch
from albumentations.augmentations.functional import smallest_max_size

from ceevee.base import AbstractPredictor
from ceevee.utils import get_relative_path, load_jit_model, to_device


class FeaturesExtractor(AbstractPredictor):
    """
    The model is a universal lightweight feature extractor.
    It was trained mostly for image similarity problem,
     though its features can be used as a baseline for other CV problems,
    """

    def __init__(self, weights_path='', cuda_id=0):
        super().__init__(cuda_id=cuda_id)
        weights_path = weights_path or get_relative_path('scene.trcd', __file__)
        self.model = to_device(load_jit_model(weights_path), cuda_id=cuda_id)
        self.resize = partial(smallest_max_size, max_size=256, interpolation=cv2.INTER_LINEAR)

    def preprocess(self, img, *kw):
        img = self.resize(img)
        h, w, _ = img.shape
        block_size = 32
        min_height = np.ceil(h / block_size).astype('int') * block_size
        min_width = np.ceil(w / block_size).astype('int') * block_size
        img = np.pad(img, ((0, min_height - h), (0, min_width - w), (0, 0)),
                     mode='constant', constant_values=0)
        x = np.transpose(img, (2, 0, 1)).astype('float32')
        return to_device(torch.from_numpy(x).unsqueeze(0),
                         cuda_id=self.cuda_id)

    def process(self, x, *kw):
        with torch.no_grad():
            vector = self.model(x)
        return vector

    def postprocess(self, x, *kw):
        return x.cpu().numpy().reshape(-1).tolist()

    def __call__(self, x, *args, **kwargs):
        x = self.preprocess(x)
        x = self.process(x)
        x = self.postprocess(x)
        return {'success': True, 'result': x}

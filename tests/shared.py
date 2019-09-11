import os
import tempfile
import unittest

import cv2
import numpy as np


class CeeveeTestCase(unittest.TestCase):
    def setUp(self):
        _, self.img_path = tempfile.mkstemp(suffix='.png')
        self.img = self._get_image()
        cv2.imwrite(self.img_path, self.img)

    def tearDown(self):
        os.remove(self.img_path)

    def _get_image(self):
        # ToDo: add real fixtures later
        return (np.random.rand(100, 100, 3) * 255).astype('uint8')

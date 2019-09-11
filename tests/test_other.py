import unittest

import numpy as np

from ceevee.utils import read_img
from tests.shared import CeeveeTestCase


class OtherTestCase(CeeveeTestCase):
    def test_read_img(self):
        img = read_img(self.img_path)
        np.testing.assert_equal(img, self.img[:, :, ::-1])


if __name__ == '__main__':
    unittest.main()

import os
import tempfile
import unittest

import cv2
import falcon
import numpy as np
from falcon import testing


class MyTestCase(testing.TestCase):
    def setUp(self):
        super(MyTestCase, self).setUp()
        from ceevee.cv_http import app
        self.app = app
        _, self.img_path = tempfile.mkstemp(suffix='.png')
        self.img = (np.random.rand(100, 100, 3) * 255).astype('uint8')
        cv2.imwrite(self.img_path, self.img)

    def tearDown(self):
        os.remove(self.img_path)

    def test_empty_post(self):
        result = testing.simulate_request(self.app, 'POST', '/dummy', params={})
        self.assertEqual(result.status, falcon.HTTP_200)
        self.assertFalse(result.json['success'])

    def test_invalid_img(self):
        result = testing.simulate_request(self.app, 'POST', '/dummy', params={'image': ''})
        self.assertEqual(result.status, falcon.HTTP_200)
        self.assertFalse(result.json['success'])
        self.assertTrue(result.json['error'].startswith('AttributeError'))

    def test_invalid_url(self):
        result = testing.simulate_request(self.app, 'POST', '/')
        self.assertEqual(result.status, falcon.HTTP_404)

    def test_valid_img(self):
        pass  # FixMe


if __name__ == '__main__':
    unittest.main()

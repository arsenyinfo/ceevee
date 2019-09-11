import unittest

import numpy as np

from ceevee import MODELS
from tests.shared import CeeveeTestCase


class ModelsTestCase(CeeveeTestCase):
    def test_models_api(self):
        for name, cls in MODELS.items():
            model = cls()

            preprocessed = model.preprocess(self.img)
            processed = model.process(preprocessed)
            postprocessed = model.postprocess(processed)

            x = model(self.img)

            self.assertTrue(isinstance(x, dict))
            self.assertEqual(x['success'], True)
            np.testing.assert_equal(x['result'], postprocessed)


if __name__ == '__main__':
    unittest.main()

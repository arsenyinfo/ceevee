import json
import subprocess
import unittest

from ceevee import MODELS
from tests.shared import CeeveeTestCase


class CliTestCase(CeeveeTestCase):
    def test_cli(self):
        for name, _ in MODELS.items():
            cmd = f'python -m ceevee.cli {name} {self.img_path}'
            x: bytes = subprocess.check_output(cmd.split(' '))
            result, = json.loads(x.decode())

            self.assertTrue(isinstance(result, dict))
            for k in ('result', 'success'):
                self.assertTrue(k in result)


if __name__ == '__main__':
    unittest.main()

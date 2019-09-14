import os
import tempfile

import falcon

from ceevee import MODELS
from ceevee.base import AbstractBaseline
from ceevee.utils import jsonify, read_img


class BaselineServer:
    def __init__(self, model: AbstractBaseline):
        self.model = model

    def _process(self, path):
        img = read_img(path)
        result = self.model(img)
        return jsonify(result)

    def on_post(self, req, resp):
        # ToDo: tests, error handling
        # ToDo: don't save to temp file
        _, suffix = req.content_type.split('/')
        assert suffix in ('jpeg', 'png')

        _, path = tempfile.mkstemp(suffix=suffix)
        with open(path, 'wb') as out:
            while True:
                chunk = req.stream.read(16384)
                if not chunk:
                    break
                out.write(chunk)

        resp.status = falcon.HTTP_200
        resp.body = self._process(path)
        os.remove(path)


tasks = set(os.environ.get('CEEVEE_TASKS', 'dummy').split(','))
models = {task: MODELS[task]() for task in tasks}
app = falcon.API()
for task, model in models.items():
    app.add_route(f'/{task}', BaselineServer(model))

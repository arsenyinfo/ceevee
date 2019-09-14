import os
import sys

import falcon
from falcon_multipart.middleware import MultipartMiddleware

from ceevee import MODELS
from ceevee.base import AbstractBaseline
from ceevee.utils import jsonify, read_img


class BaselineServer:
    def __init__(self, model: AbstractBaseline):
        self.model = model

    def _run_model(self, path):
        img = read_img(path)
        result = self.model(img)
        return jsonify(result)

    def _process(self, img, resp):
        fname = img.filename

        with open(fname, 'wb') as out:
            out.write(img.file.read())
        resp.body = self._run_model(fname)
        resp.status = falcon.HTTP_200
        os.remove(fname)

    def on_post(self, req, resp):
        img = req.get_param('image')
        if img is None:
            resp.body = jsonify({'success': False, 'error': 'Image not found'})
            return
        try:
            self._process(img, resp)
        except Exception:
            ex_type, ex_value, ex_traceback = sys.exc_info()
            resp.body = jsonify({'success': False, 'error': f'{ex_type.__name__}: {ex_value}'})


tasks = set(os.environ.get('CEEVEE_TASKS', 'dummy').split(','))
models = {task: MODELS[task]() for task in tasks}
app = falcon.API(middleware=[MultipartMiddleware()])

for task, model in models.items():
    app.add_route(f'/{task}', BaselineServer(model))

from wsgiref.simple_server import make_server

import falcon
from fire import Fire

from ceevee import MODELS
from ceevee.base import AbstractBaseline
from ceevee.utils import jsonify, read_img


class BaselineServer:
    def __init__(self, model: AbstractBaseline):
        self.model = model

    def _process(self, path, resp):
        resp.status = falcon.HTTP_200
        img = read_img(path)
        result = self.model(img)
        resp.body = jsonify(result)

    def on_get(self, req, resp):
        params = req.params
        if 'img' in params:
            self._process(params['img'], resp)
        else:
            resp.status = falcon.HTTP_400
            raise KeyError('Expected GET parameter `img`')


def main(port, *tasks):
    tasks = set(tasks)
    models = {task: MODELS[task]() for task in tasks}
    app = falcon.API()
    for task, model in models.items():
        app.add_route(f'/{task}', BaselineServer(model))

    return app, tasks, port


if __name__ == '__main__':
    app, tasks, port = Fire(main)
    with make_server('', port, app) as httpd:
        print(f'Tasks ({", ".join(tasks)}) are being served on port {port}')
        httpd.serve_forever()

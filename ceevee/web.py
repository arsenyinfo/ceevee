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


def main(task):
    model = MODELS[task]()
    app = falcon.API()
    app.add_route('/', BaselineServer(model))
    return app, task


if __name__ == '__main__':
    # ToDo: make multiple APIs at a time
    app, task = Fire(main)
    with make_server('', 8193, app) as httpd:
        print(f'Task {task} is being served on port 8193')
        httpd.serve_forever()

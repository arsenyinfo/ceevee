from typing import Union

import cv2
import torch
import ujson as json
import yaml


def load_yaml(x: str):
    with open(x) as fd:
        return yaml.load(fd, yaml.FullLoader)


def ensure_dict(x: Union[str, dict]):
    if isinstance(x, dict):
        return x
    return load_yaml(x)


def to_device(x):
    return x.cuda() if torch.cuda.is_available() else x


def load_jit_model(x):
    return torch.jit.load(x, map_location='cuda:0' if torch.cuda.is_available() else 'cpu')


def read_img(x: str):
    return cv2.imread(x)[:, :, ::-1]


def jsonify(x):
    # ToDo: process numpy arrays
    return json.dumps(x)

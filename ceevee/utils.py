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
    img = cv2.imread(x)
    if len(img.shape) == 3:  # BGR -> RGB
        img = img[:, :, ::-1]
    elif len(img.shape) < 3:  # grayscale -> RGB
        img = np.expand_dims(img, -1)
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

    return 


def jsonify(x):
    # ToDo: process numpy arrays
    return json.dumps(x)

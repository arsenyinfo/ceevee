[![Build status](https://badge.buildkite.com/3be2c7533d11e157a0b1fef8af1231356349694c459f072ccc.svg)](https://buildkite.com/ceevee/ceevee-tests)

# ceevee

`ceevee` (read like CV, i.e. computer vision) is a Python library for various computer vision problems with a focus on easy usage.

`ceevee` aims to be a bridge between deep learning practitioners training accurate models and product-oriented software engineers who just want to process their images instead of diving into the deep learning ecosystem.

Python 3.6+ is supported.

## Install

From PyPI - not available yet

From source
```
python setup.py bdist_wheel
pip install -U ceevee-0.0.1-py3-none-any.whl
```

## Tasks

## Usage

All tasks shares the same API

### CLI API

`python -m ceevee.cli task /path/to/img1.jpg /path/to/img2.jpg ... /path/to/imgN.jpg > result.json`

### HTTP API

HTTP API is based on [Falcon](https://github.com/falconry/falcon),
so it can be used with any WSGI server, such as uWSGI or Gunicorn.

- install your favourite WSGI server (e.g. `pip install gunicorn`)
- set env variable `CEEVEE_TASKS` for your tasks,
 multiple comma separated tasks are supported, e.g. `CEEVEE_TASKS=task1,task2` 
- run a server `CEEVEE_TASKS=dummy gunicorn ceevee.cv_http`;
- send a POST request using correct `Content-Type`. 
Example using [httpie](https://httpie.org/): 
`CEEVEE_TASKS="dummy" http POST localhost:8000/dummy Content-Type:image/png < /tmp/gray.png`)

!ToDo: add more detailed example

### Python API

```python
from ceevee.utils import read_img
from ceevee.dummy import DummyBaseline
baseline = DummyBaseline()
img = read_img('/path/to/img.jpg')
result = baseline(img)
```

## Contributions

Yes, you can add a new model!

### Checklist:
- create a GitHub issue with your suggested model;
- create a new Baseline class (see `ceevee.dummy.DummyBaseline`) and implement three methods (`preprocess`, `process`, 
`postprocess`);
- add your model to `MODELS` at `ceevee/__init__.py`
- add tests to `tests/`;
- once CI is green, create a pull request!

# ToDo:

- infrastructure:
    - packaging, pip
- APIs:
    - http: tests, error handling 
- models: 
    - face detection
    - face emotion
    - face keypoints 
    - car detection
    - crowd density estimation 

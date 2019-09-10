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

- run a server `python -m ceevee.web task`; 
- send a GET request `host:port/?img=path/to/img` (local and remote paths) are supported

HTTP API is based on [Falcon](https://github.com/falconry/falcon), 
so it can be used with any WSGI server, such as uWSGI or Gunicorn. 

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
- tests
- CI 
- packaging, pip
- http: remote files
- http: files from body
- http: multiple apis at a time
- http: configurable port 
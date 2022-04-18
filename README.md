# Image Subtractor User Interface

<p>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
<a href="https://github.com/lycantrope/imagesubtractor/blob/main/License"><img alt="license: GPL-3.0" src="https://img.shields.io/github/license/lycantrope/imagesubtractor.svg"></a>
</p>

This application is code refactoring from `imagesubtandmeasure.py` that created by Taizo Kawano.

## Requirements

- python >= 3.7.10
- opencv-python-headless
- pandas
- numpy
- PySide2


## Installation and running

### pip environment (Linux/mac)
- Installation:
```shell
~$ python3 -m venv .venv

~$ source .venv/bin/activate

(.venv) ~$ pip install -U git+https://github.com/lycantrope/imagesubtractor
```
- Running application:

```shell
~$ source .venv/bin/activate
~$ imagesubtractor
```

### pip environment (Windows)
- Installation:

```shell
(PS) ~$ python3 -m venv .venv

(PS) ~$ source .venv\Scripts\activate.bat

(PS)(.venv) ~$ pip install -U git+https://github.com/lycantrope/imagesubtractor
```
- Running application:

```shell
(PS) ~$ source .venv\Scripts\activate.bat
(PS) ~$ imagesubtractor
```

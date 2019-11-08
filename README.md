# FRAUD DETECTION 

This is a machine learning project of being able to predict whether a transaction is a fraud or not.
Take note the Dataset is taken from [zindi](zindi.africa) from a closed competition.

## Contributor

[DeveloperPrince](developerprince.co.zw)

## Requirements
    1. Python 3.7
    2. pip
    3. [Virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

## Setup & Inference

1. create virtual env

on Unix based System
```bash
    python3 -m venv env
```
or Win32

```bash
    py -m venv env
```
2. Switch to virtual env

on Unix based System
```bash
    source env/bin/activate
```

or Win32 

```bash
.\env\Scripts\activate
```

3. Create a Model

```bash
    python3 train.py
```

4. Infer Model

```bash
    python3 main.py infer json [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12] [13] [14] [15]
```

Enjoy
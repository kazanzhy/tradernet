# Tradernet API
[![Upload to PyPI](https://github.com/kazanzhy/tradernet/actions/workflows/pypi-publish.yml/badge.svg)](https://github.com/kazanzhy/tradernet/actions/workflows/pypi-publish.yml)
[![PyPI version](https://badge.fury.io/py/tradernet.svg)](https://badge.fury.io/py/tradernet)


[![PyPi version](https://pypip.in/v/$REPO/badge.png)](https://crate.io/packages/$REPO/)
[![PyPi downloads](https://pypip.in/d/$REPO/badge.png)](https://crate.io/packages/$REPO/)


## Description
This Python package is unofficial wrapper for Tradernet Public API.  
More details in [Tradernet official documentation](https://tradernet.com/tradernet-api/).

## Installation
```shell
pip install tradernet
```

## Usage
```python
import tradernet as NtApi

pub_ = 'Your Api key'
sec_ = 'Your Api secret'

res = NtApi.PublicApiClient(pub_, sec_, NtApi.PublicApiClient().V2)
res.sendRequest(<command>, <params>).content.decode("utf-8")
```

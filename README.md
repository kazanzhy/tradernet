# Tradernet API
[![Upload to PyPI](https://github.com/kazanzhy/tradernet/actions/workflows/pypi-publish.yml/badge.svg)](https://github.com/kazanzhy/tradernet/actions/workflows/pypi-publish.yml)

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

## Details
More details in `Tradernet official documentation <https://tradernet.com/tradernet-api/>`_.
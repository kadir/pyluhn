# pyluhn


## Installation

Use `pip install pyluhn` or `python setup.py install`.

## Usage

`verify` checks whether the given string is a valid
Luhn string in the given base. By default, base is 10:

```python
>>> from pyluhn import verify
>>> verify('5105105105105100') # MasterCard Test Card
True
>>> verify('5105105105105101') # Test Number
False
```

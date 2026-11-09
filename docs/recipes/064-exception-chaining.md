# Preserve the cause of a translated exception

A standalone Python 3.10+ recipe. Run the snippet with Python; its assertion verifies the result.

```python
try:
    try:
        int('invalid')
    except ValueError as error:
        raise RuntimeError('Invalid count') from error
except RuntimeError as error:
    assert isinstance(error.__cause__, ValueError)
```

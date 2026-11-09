# Invert a dictionary with unique values

A standalone Python 3.10+ recipe. Run the snippet with Python; its assertion verifies the result.

```python
assert {v: k for k, v in {'a': 1, 'b': 2}.items()} == {1: 'a', 2: 'b'}
```

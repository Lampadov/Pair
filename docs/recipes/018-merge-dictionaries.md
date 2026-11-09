# Merge dictionaries with override precedence

A standalone Python 3.10+ recipe. Run the snippet with Python; its assertion verifies the result.

```python
assert ({'a': 1, 'b': 2} | {'b': 3}) == {'a': 1, 'b': 3}
```

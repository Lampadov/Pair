# Unpack the first and remaining values

A standalone Python 3.10+ recipe. Run the snippet with Python; its assertion verifies the result.

```python
first, *rest = [1, 2, 3]
assert first == 1 and rest == [2, 3]
```

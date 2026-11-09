# Partition a key and value

A standalone Python 3.10+ recipe. Run the snippet with Python; its assertion verifies the result.

```python
assert 'name=Pair'.partition('=') == ('name', '=', 'Pair')
```

# Remove duplicates while retaining order

A standalone Python 3.10+ recipe. Run the snippet with Python; its assertion verifies the result.

```python
assert list(dict.fromkeys(['b', 'a', 'b'])) == ['b', 'a']
```

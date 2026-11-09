# Flatten one nesting level

A standalone Python 3.10+ recipe. Run the snippet with Python; its assertion verifies the result.

```python
rows = [[1, 2], [], [3]]
assert [x for row in rows for x in row] == [1, 2, 3]
```

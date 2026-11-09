# Sort records by a field

A standalone Python 3.10+ recipe. Run the snippet with Python; its assertion verifies the result.

```python
rows = [{'n': 2}, {'n': 1}]
assert sorted(rows, key=lambda row: row['n']) == [{'n': 1}, {'n': 2}]
```

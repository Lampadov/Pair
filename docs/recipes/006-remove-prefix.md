# Remove a known prefix

A standalone Python 3.10+ recipe. Run the snippet with Python; its assertion verifies the result.

```python
assert 'refs/heads/main'.removeprefix('refs/heads/') == 'main'
```

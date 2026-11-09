# Choose unordered pairs

A standalone Python 3.10+ recipe. Run the snippet with Python; its assertion verifies the result.

```python
from itertools import combinations
assert list(combinations([1, 2, 3], 2)) == [(1, 2), (1, 3), (2, 3)]
```

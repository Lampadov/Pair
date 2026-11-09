# Visit neighboring values

A standalone Python 3.10+ recipe. Run the snippet with Python; its assertion verifies the result.

```python
from itertools import pairwise
assert list(pairwise([1, 2, 4])) == [(1, 2), (2, 4)]
```

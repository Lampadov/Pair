# Chain multiple iterables

A standalone Python 3.10+ recipe. Run the snippet with Python; its assertion verifies the result.

```python
from itertools import chain
assert list(chain([1, 2], [3])) == [1, 2, 3]
```

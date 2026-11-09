# Cache a deterministic function

A standalone Python 3.10+ recipe. Run the snippet with Python; its assertion verifies the result.

```python
from functools import cache
@cache
def square(n):
    return n * n
assert square(4) == square(4) == 16
assert square.cache_info().hits == 1
```

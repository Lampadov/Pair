# Select the smallest values

A standalone Python 3.10+ recipe. Run the snippet with Python; its assertion verifies the result.

```python
from heapq import nsmallest
assert nsmallest(2, [5, 1, 4, 2]) == [1, 2]
```

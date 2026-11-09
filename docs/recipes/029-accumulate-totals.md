# Compute running totals

A standalone Python 3.10+ recipe. Run the snippet with Python; its assertion verifies the result.

```python
from itertools import accumulate
assert list(accumulate([2, 3, 4])) == [2, 5, 9]
```

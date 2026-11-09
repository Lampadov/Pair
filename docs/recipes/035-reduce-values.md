# Reduce values with a binary operation

A standalone Python 3.10+ recipe. Run the snippet with Python; its assertion verifies the result.

```python
from functools import reduce
from operator import mul
assert reduce(mul, [2, 3, 4], 1) == 24
```

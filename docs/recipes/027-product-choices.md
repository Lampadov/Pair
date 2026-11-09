# Generate a Cartesian product

A standalone Python 3.10+ recipe. Run the snippet with Python; its assertion verifies the result.

```python
from itertools import product
assert list(product('ab', [1, 2])) == [('a', 1), ('a', 2), ('b', 1), ('b', 2)]
```

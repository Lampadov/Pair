# Take a bounded part of a generator

A standalone Python 3.10+ recipe. Run the snippet with Python; its assertion verifies the result.

```python
from itertools import count, islice
assert list(islice(count(10), 3)) == [10, 11, 12]
```

# Group consecutive equal keys

A standalone Python 3.10+ recipe. Run the snippet with Python; its assertion verifies the result.

```python
from itertools import groupby
assert {k: list(g) for k, g in groupby(sorted('baba'))} == {'a': ['a', 'a'], 'b': ['b', 'b']}
```

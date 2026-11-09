# Sort tuples by an indexed field

A standalone Python 3.10+ recipe. Run the snippet with Python; its assertion verifies the result.

```python
from operator import itemgetter
assert sorted([('a', 2), ('b', 1)], key=itemgetter(1)) == [('b', 1), ('a', 2)]
```

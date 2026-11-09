# Group records with a default dictionary

A standalone Python 3.10+ recipe. Run the snippet with Python; its assertion verifies the result.

```python
from collections import defaultdict
groups = defaultdict(list)
for key, value in [('a', 1), ('b', 2), ('a', 3)]:
    groups[key].append(value)
assert dict(groups) == {'a': [1, 3], 'b': [2]}
```

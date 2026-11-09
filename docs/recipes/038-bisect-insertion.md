# Insert into a sorted list

A standalone Python 3.10+ recipe. Run the snippet with Python; its assertion verifies the result.

```python
from bisect import insort
values = [1, 3, 5]
insort(values, 4)
assert values == [1, 3, 4, 5]
```

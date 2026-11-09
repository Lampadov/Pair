# Keep a bounded window of values

A standalone Python 3.10+ recipe. Run the snippet with Python; its assertion verifies the result.

```python
from collections import deque
window = deque([1, 2], maxlen=2)
window.append(3)
assert list(window) == [2, 3]
```

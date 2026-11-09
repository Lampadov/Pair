# Represent a value with a frozen dataclass

A standalone Python 3.10+ recipe. Run the snippet with Python; its assertion verifies the result.

```python
from dataclasses import dataclass
@dataclass(frozen=True)
class Point:
    x: int
    y: int
assert Point(1, 2) == Point(x=1, y=2)
```

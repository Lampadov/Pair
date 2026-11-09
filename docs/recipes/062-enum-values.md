# Define named constant values

A standalone Python 3.10+ recipe. Run the snippet with Python; its assertion verifies the result.

```python
from enum import Enum
class Status(Enum):
    OPEN = 'open'
    CLOSED = 'closed'
assert Status('open') is Status.OPEN
```

# Use a context-managed text buffer

A standalone Python 3.10+ recipe. Run the snippet with Python; its assertion verifies the result.

```python
from io import StringIO
with StringIO() as buffer:
    buffer.write('pair')
    assert buffer.getvalue() == 'pair'
assert buffer.closed
```

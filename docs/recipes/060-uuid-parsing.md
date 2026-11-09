# Parse and normalize a UUID

A standalone Python 3.10+ recipe. Run the snippet with Python; its assertion verifies the result.

```python
from uuid import UUID
value = UUID('12345678-1234-5678-1234-567812345678')
assert value.hex == '12345678123456781234567812345678'
```

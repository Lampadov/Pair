# Convert a timestamp between time zones

A standalone Python 3.10+ recipe. Run the snippet with Python; its assertion verifies the result.

```python
from datetime import datetime, timezone, timedelta
value = datetime(2026, 11, 9, 9, tzinfo=timezone.utc)
assert value.astimezone(timezone(timedelta(hours=3))).hour == 12
```

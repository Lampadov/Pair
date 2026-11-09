# Add a duration to a date

A standalone Python 3.10+ recipe. Run the snippet with Python; its assertion verifies the result.

```python
from datetime import date, timedelta
assert date(2026, 11, 9) + timedelta(days=7) == date(2026, 11, 16)
```

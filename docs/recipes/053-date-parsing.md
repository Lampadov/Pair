# Parse an ISO date

A standalone Python 3.10+ recipe. Run the snippet with Python; its assertion verifies the result.

```python
from datetime import date
assert date.fromisoformat('2026-11-09').year == 2026
```

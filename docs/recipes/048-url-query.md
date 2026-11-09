# Encode URL query parameters

A standalone Python 3.10+ recipe. Run the snippet with Python; its assertion verifies the result.

```python
from urllib.parse import urlencode, parse_qs
query = urlencode({'q': 'pair work', 'page': 2})
assert parse_qs(query) == {'q': ['pair work'], 'page': ['2']}
```

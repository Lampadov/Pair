# Parse URL components

A standalone Python 3.10+ recipe. Run the snippet with Python; its assertion verifies the result.

```python
from urllib.parse import urlsplit
parts = urlsplit('https://example.com/recipes?q=pair')
assert (parts.scheme, parts.hostname, parts.path) == ('https', 'example.com', '/recipes')
```

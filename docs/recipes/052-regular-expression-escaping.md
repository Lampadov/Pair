# Match literal special characters

A standalone Python 3.10+ recipe. Run the snippet with Python; its assertion verifies the result.

```python
import re
assert re.fullmatch(re.escape('a+b'), 'a+b') is not None
```

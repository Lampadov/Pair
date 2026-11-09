# Bind a function argument

A standalone Python 3.10+ recipe. Run the snippet with Python; its assertion verifies the result.

```python
from functools import partial
parse_binary = partial(int, base=2)
assert parse_binary('101') == 5
```

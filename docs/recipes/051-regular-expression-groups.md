# Extract named regular expression groups

A standalone Python 3.10+ recipe. Run the snippet with Python; its assertion verifies the result.

```python
import re
match = re.fullmatch(r'(?P<name>[A-Za-z]+)-(?P<number>[0-9]+)', 'Pair-64')
assert match.groupdict() == {'name': 'Pair', 'number': '64'}
```

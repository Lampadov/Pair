# Encode and decode JSON

A standalone Python 3.10+ recipe. Run the snippet with Python; its assertion verifies the result.

```python
import json
value = {'pair': ['Alice', 'Bob']}
assert json.loads(json.dumps(value)) == value
```

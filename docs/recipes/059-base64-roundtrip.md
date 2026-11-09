# Encode and decode Base64

A standalone Python 3.10+ recipe. Run the snippet with Python; its assertion verifies the result.

```python
from base64 import b64encode, b64decode
assert b64encode(b'pair') == b'cGFpcg=='
assert b64decode(b'cGFpcg==', validate=True) == b'pair'
```

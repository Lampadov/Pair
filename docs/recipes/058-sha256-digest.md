# Compute a SHA-256 digest

A standalone Python 3.10+ recipe. Run the snippet with Python; its assertion verifies the result.

```python
from hashlib import sha256
assert sha256(b'abc').hexdigest() == 'ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad'
```

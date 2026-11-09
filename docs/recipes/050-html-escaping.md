# Escape HTML special characters

A standalone Python 3.10+ recipe. Run the snippet with Python; its assertion verifies the result.

```python
from html import escape
assert escape('<pair> &') == '&lt;pair&gt; &amp;'
```

# Parse CSV records with quoted fields

A standalone Python 3.10+ recipe. Run the snippet with Python; its assertion verifies the result.

```python
import csv
from io import StringIO
rows = list(csv.DictReader(StringIO('name,note\nAlice,"one,two"\n')))
assert rows == [{'name': 'Alice', 'note': 'one,two'}]
```

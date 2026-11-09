# Create and clean up a temporary directory

A standalone Python 3.10+ recipe. Run the snippet with Python; its assertion verifies the result.

```python
from pathlib import Path
from tempfile import TemporaryDirectory
with TemporaryDirectory() as folder:
    path = Path(folder) / 'note.txt'
    path.write_text('pair', encoding='utf-8')
    assert path.read_text(encoding='utf-8') == 'pair'
assert not Path(folder).exists()
```

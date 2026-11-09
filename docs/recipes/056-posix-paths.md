# Inspect a path without accessing a filesystem

A standalone Python 3.10+ recipe. Run the snippet with Python; its assertion verifies the result.

```python
from pathlib import PurePosixPath
path = PurePosixPath('docs/recipe.md')
assert (path.parent.as_posix(), path.stem, path.suffix) == ('docs', 'recipe', '.md')
```

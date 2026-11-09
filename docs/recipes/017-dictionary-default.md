# Read a dictionary with a default

A standalone Python 3.10+ recipe. Run the snippet with Python; its assertion verifies the result.

```python
settings = {'theme': 'dark'}
assert settings.get('language', 'en') == 'en'
```

### Python reference copy
Mutable types need reference copy. List, dictionary are mutable. String, tuple are immutable.

Use list as an example:
```python
a.append(b.copy()) (when b will change)
or
a.append(b[:]) (when b will change)

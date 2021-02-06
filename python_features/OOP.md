
### Class variable and instance variable
```python
class Shark:
    animal_type = "fish" # class variable
    def __init__(self, name, age):
        self.name = name # can be acessed from outside
        age = age # can NOT be acessed from outside
```

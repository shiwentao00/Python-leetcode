### Mutable vs Immutable

In Python, some of the objects are mutable while some are immutable. This is a very important concept. Mutable objects such as list and dict is not hashable, while immutable objects such as tuple and integer are hashable, thus can be used as keys of dictionary or can be put in set.

For instances of custom classes, they will have a hash value defined at creation and it will not change over time, for example:
```python
# this example is from https://www.pythonforthelab.com/blog/what-are-hashable-objects/
class MyClass:
    def __init__(self, value):
        self.value = value

my_obj = MyClass(1)
print(my_obj.__hash__()) # 8757243744113
my_new_obj = MyClass(1)
print(my_new_obj.__hash__()) # -9223363279611078919
```

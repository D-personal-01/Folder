import numpy as np

numpy_functions = [
    name for name in dir(np)
    if callable(getattr(np, name)) and not name.startswith('_')
]

print(numpy_functions)

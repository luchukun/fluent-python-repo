from functools import partial
from operator import mul
triple = partial(mul, 3)
print ('triple(3) is',triple(3))

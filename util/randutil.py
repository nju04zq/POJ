import random

random.seed()

_RANDINT_MIN_ = 0
_RANDINT_MAX_ = 100

def randint(min_int=None, max_int=None):
    if min_int is None:
        min_int = _RANDINT_MIN_
    if max_int is None:
        max_int = _RANDINT_MAX_
    return random.randint(min_int, max_int)

def randint_array(min_int=None, max_int=None, size=None):
    if min_int is None:
        min_int = _RANDINT_MIN_
    if max_int is None:
        max_int = _RANDINT_MAX_
    if size is None:
        size = randint(min_int=0, max_int=63)
    array = [randint(min_int, max_int) for i in xrange(size)]
    return array

def randint_sorted_array(min_int=None, max_int=None, size=None, reverse=False):
    array = randint_array(min_int, max_int, size)
    array.sort(reverse=reverse)
    return array


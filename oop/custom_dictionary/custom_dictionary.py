from collections import UserDict

class UperClassDict(dict):
    def __setitem__(self, key, value):
        key = key.upper()
        super().__setitem__(key, value)

nb = UperClassDict()

# This only work with setitem
nb['one'] = 1
# {'ONE': 1}

# Doenst work with Initialization
nb = UperClassDict({'one': 1, 'two': 2}) 
# {'one': 1, 'two': 2}

# Update
nb.update({'one': 'one_lower'})
# {'one': 'one_lower', 'two': 2}

# Or setdefault
nb.setdefault('set', 'default')
# {'one': 'one_lower', 'two': 2, 'set': 'default'}


# To solve this problem we need to set it in the __init__
class UpperCaseDict(dict):
    def __init__(self, mapping=None, /, **kwargs):
        if mapping is not None:
            mapping = {
                str(key).upper(): value for key, value in mapping.items()
            }
        else:
            mapping = {}
        if kwargs:
            mapping.update(
                {str(key).upper(): value for key, value in kwargs.items()}
            )
        super().__init__(mapping)

    # nb['hi'] = 'hello' - > {'HI': 'hello'}
    def __setitem__(self, key, value):
        key = key.upper()
        super().__setitem__(key, value)


nb = UpperCaseDict({'one': 1, 'two': 2})

nb['ola'] = 'nb'
nb.update({'ola': 'ola_lower'})


class UpperCaseDict2(UserDict):
    def __setitem__(self, key, item) -> None:
        key = key.upper()
        return super().__setitem__(key, item)


nb = UpperCaseDict2({'one': 1, 'two': 2})

nb["three"] = 3
nb.update({"four": 4})
nb.setdefault("five", 5)
# {'ONE': 1, 'TWO': 2, 'THREE': 3, 'FOUR': 4, 'FIVE': 5}


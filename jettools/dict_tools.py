from typing import Dict, List, Union, TypeVar
from jettools.validation import are_valid_args, Validator

K = TypeVar('K')
V = TypeVar('V')


def get(d: Union[Dict[K, V], Dict[K, Dict]], k: Union[List[K], K]) -> Union[None, V]:
    """
    Get the value of a key or nested keys in a dictionary, returning None if it doesn't exist.
    :param d: dictionary to look in
    :param k: key or list of keys
    :return: an item in the dictionary, or None
    """
    if not isinstance(k, list):
        return d.get(k)

    if len(k) == 0:
        return None

    res = d
    for key in k:
        if res is None or not isinstance(res, dict):
            return None
        res = res.get(key)

    return res


def append_to_key_list(d: Dict[K, List[V]], k: K, v: V) -> None:
    """
    Add an item to a key: [value] list. If it does not yet exist, create it.
    :param d: dictionary containing the lists
    :param k: key for the list
    :param v: value to append to the list
    """
    dict_check = lambda x: isinstance(x, dict) and all([isinstance(x[key], List) for key in x])
    is_valid = are_valid_args(Validator('d', d, dict_check))
    if not is_valid:
        raise ValueError('Invalid arguments:', is_valid.message)

    if d.get(k) is None:
        d[k] = []
    d[k].append(v)


def increment_key(d: Dict[K, int], k: K, by: Union[int, float] = 1) -> None:
    """
    Increment a key (in place) by the specified amount.
    :param d: dictionary containing the accumulators
    :param k: key to increment
    :param by: amount to increment the key by
    """
    dict_check = lambda x: isinstance(x, dict) and \
                           all([isinstance(x[key], int) or isinstance(x[key], float) for key in x])
    is_valid = are_valid_args([
        Validator('d', d, dict_check),
        Validator('by', by, lambda b: isinstance(b, int) or isinstance(b, float)),
    ])
    if not is_valid:
        raise ValueError('Invalid arguments, cannot increment key: ' + is_valid.message)

    if d.get(k) is None:
        d[k] = 0
    d[k] += by


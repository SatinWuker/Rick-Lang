"""
Common/Shared utilities, to use across multiple modules/scripts
"""
from os.path import splitext

def starts_ends(container: str | list, x):
    """
    Check if it starts and ends with the same value.

    Examples:
    ```
    starts_ends('"rick"', '"') # `True`
    starts_ends('"rick"', "'") # `False`
    starts_ends('(rick)', '()') # `False`
    ```
    """
    return container[0] == x and container[-1] == x

def join_list(l: list):
    """Convert any `list` into a `str` without delimiter."""
    return ''.join(map(str, l))

def remove_all(l: list, x):
    """Remove all occurrences of value (in-place) from a `list` and return it."""
    while x in l:
        l.remove(x)
    return l

def filter_str(s: str):
    """Remove 1st and last chars from a `str`."""
    return s[1:-1]

def remove_path_ext(f_name: str):
    """
    Return a file-name-path without extension (substring after last dot).

    Examples:
    ```
    remove_path_ext('Never Gonna Give U Up.ogg') # 'Never Gonna Give U Up'

    remove_path_ext('totally-not-a-rickroll.exe') # 'totally-not-a-rickroll'

    remove_path_ext('.rick') # '.rick'
    ```
    """
    (f_name, _) = splitext(f_name)
    return f_name

def precedence(op: str):
    """
    Get precedence of basic arithmetic operators (+ - * /).

    `op` should be a char.

    returns `1` for lowest precedence, `2` for highest, `0` if `op` is not recognized.
    """
    if op in {'+', '-'}:
        return 1
    if op in {'*', '/'}:
        return 2
    return 0

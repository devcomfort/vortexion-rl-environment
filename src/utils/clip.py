"""
Clip values to a specified range.

This module provides a function to clamp numeric values between
minimum and maximum bounds, with optional numpy support.
"""

try:
    import numpy as np

    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False


def clip(value, min_val, max_val):
    """
    Clip a value to be within the specified range.

    This function constrains a value to lie between min_val and max_val.
    If numpy is available, it uses np.clip for better performance.
    Otherwise, it falls back to using Python's built-in min/max functions.

    Parameters
    ----------
    value : int or float or array_like
        The value(s) to clip. Can be a scalar or array-like.
    min_val : int or float or None
        Minimum allowed value. Values below this will be set to min_val.
        If None, no minimum limit is applied.
    max_val : int or float or None
        Maximum allowed value. Values above this will be set to max_val.
        If None, no maximum limit is applied.

    Returns
    -------
    int or float or ndarray
        The clipped value(s). Returns the same type as input if scalar,
        or numpy array if numpy is available and input is array-like.

    Examples
    --------
    >>> clip(15, 0, 10)
    10
    >>> clip(-5, 0, 10)
    0
    >>> clip(5, 0, 10)
    5
    >>> clip(15, 0, None)
    15
    >>> clip(-5, None, 10)
    -5
    >>> clip([1, 5, 15, -5], 0, 10)
    [1, 5, 10, 0]

    Notes
    -----
    If numpy is available and the input is array-like, the result will
    be a numpy array. Otherwise, the result will be a Python scalar or list.
    """
    if HAS_NUMPY:
        return np.clip(value, min_val, max_val)

    # Fallback without numpy
    if max_val is None:
        if min_val is None:
            return value
        return max(min_val, value)
    elif min_val is None:
        return min(value, max_val)
    return max(min_val, min(max_val, value))

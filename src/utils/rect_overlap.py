"""
Check if two rectangles overlap.

This function determines whether two axis-aligned rectangles intersect
by checking if their bounding boxes overlap in both x and y dimensions.
"""


def rect_overlap(x1, y1, w1, h1, x2, y2, w2, h2):
    """
    Check if two rectangles overlap.

    Two rectangles overlap if they share any common area. This function
    checks for overlap by comparing the boundaries of both rectangles
    in both horizontal and vertical dimensions.

    Parameters
    ----------
    x1 : int or float
        X coordinate of the first rectangle's top-left corner.
    y1 : int or float
        Y coordinate of the first rectangle's top-left corner.
    w1 : int or float
        Width of the first rectangle.
    h1 : int or float
        Height of the first rectangle.
    x2 : int or float
        X coordinate of the second rectangle's top-left corner.
    y2 : int or float
        Y coordinate of the second rectangle's top-left corner.
    w2 : int or float
        Width of the second rectangle.
    h2 : int or float
        Height of the second rectangle.

    Returns
    -------
    bool
        True if the rectangles overlap, False otherwise.

    Examples
    --------
    >>> rect_overlap(0, 0, 10, 10, 5, 5, 10, 10)
    True
    >>> rect_overlap(0, 0, 10, 10, 20, 20, 10, 10)
    False
    >>> rect_overlap(0, 0, 10, 10, 10, 0, 10, 10)
    False
    >>> rect_overlap(0, 0, 10, 10, 9, 0, 10, 10)
    True
    """
    return x1 < x2 + w2 and x1 + w1 > x2 and y1 < y2 + h2 and y1 + h1 > y2


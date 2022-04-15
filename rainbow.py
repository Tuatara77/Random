def rainbow(rgb: tuple, minbrightness: int=0, maxbrightness: int=0, changerate: int=3):
    assert len(rgb) == 3 and rgb[0] == int(rgb[0]) and rgb[1] == int(rgb[1]) and rgb[2] == int(rgb[2]), "Tuple must be 3 integers"
    assert rgb[0] == maxbrightness or rgb[1] == maxbrightness or rgb[2] == maxbrightness and \
           rgb[0] == minbrightness or rgb[1] == minbrightness or rgb[2] == minbrightness, "There must be values which are equal to the min and max brightness"
    r, g, b = rgb

    if                   r <  maxbrightness and                 g == minbrightness and                 b == maxbrightness: r += changerate
    elif minbrightness < r <= maxbrightness and                 g == maxbrightness and                 b == minbrightness: r -= changerate
    elif                 r == maxbrightness and                 g <  maxbrightness and                 b == minbrightness: g += changerate
    elif                 r == minbrightness and minbrightness < g <= maxbrightness and                 b == maxbrightness: g -= changerate
    elif                 r == minbrightness and                 g == maxbrightness and                 b <  maxbrightness: b += changerate
    elif                 r == maxbrightness and                 g == minbrightness and minbrightness < b <= maxbrightness: b -= changerate

    if r <= minbrightness: r = minbrightness
    if r >= maxbrightness: r = maxbrightness
    if g <= minbrightness: g = minbrightness
    if g >= maxbrightness: g = maxbrightness
    if b <= minbrightness: b = minbrightness
    if b >= maxbrightness: b = maxbrightness

    return (r,g,b)

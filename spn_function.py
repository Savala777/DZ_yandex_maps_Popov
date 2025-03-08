def count_spn(bounds):
    lower_corner, upper_corner = (list(map(float, bounds['lowerCorner'].split())),
                                  list(map(float, bounds['upperCorner'].split())))
    delta = [str(upper_corner[0] - lower_corner[0]), str(upper_corner[1] - lower_corner[1])]
    return delta

def get_float_range(start, end, step):
    res = []
    while(start < end):
        res.append(start)
        start = start + step
    return res

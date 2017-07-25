def missing_power(unresolved, m, count):
    """
    Function interpolating missing value from measurements of power
    with convert to integer
    :param unresolved: list with n data from measurements
    :param m: maximum number of missing elements to interpolate
    :param count: number of missings in previous list
    :return: resolved list with n data with interpolated missing data
    """

    resolved = [0 for _ in range(len(unresolved))]
    if unresolved[0] == "missing" or unresolved[0] == "":
        resolved[0] = "-95"
    if unresolved[-1] == "missing" or unresolved[-1] == "":
        if 0 <= count < m:
            resolved[-1] = int(unresolved[-2])
        if count >= m:
            resolved[-1] = int(-95)
        count += 1
    else:
        resolved[-1] = int(unresolved[-1])
        count = 0

    for i in range(len(unresolved)-1):
            resolved[i] = int(unresolved[i])
    return resolved, count


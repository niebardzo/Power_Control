def missing_power(unresolved, m, count):
    """
    Function interpolating missing value from measurements of power
    with convertion to integer
    :param unresolved: list with n data from measurements
    :param m: maximum number of missing elements to interpolate
    :param count: number of missings in previous list
    :return: resolved list with n data with interpolated missing data
    """

    resolved = [0 for _ in range(len(unresolved))]
    if unresolved[0] == "missing" or unresolved[0] == "":
        resolved[0] = "-95"
    for i in range(len(unresolved)):
        if unresolved[i] == "missing" or unresolved[i] == "":
            count += 1
            if 1 <= count <= m:
                resolved[i] = int(unresolved[i-1])
            if count > m:
                resolved[i] = -95
        else:
            resolved[i] = int(unresolved[i])
            count = 0
    return resolved, count

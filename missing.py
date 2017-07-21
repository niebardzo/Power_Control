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
    if unresolved[len(unresolved)-1] == "missing" or unresolved[len(unresolved)-1] == "":
        if 1 <= count <= m:
            resolved[len(resolved)-1] = int(unresolved[len(resolved)-2])
        if count > m:
            resolved[len(resolved)-1] = int(-95)
        count += 1
    else:
        resolved[len(resolved) - 1] = int(unresolved[len(resolved)-1])
        count = 0

    for i in range(len(unresolved)-1):
            resolved[i] = int(unresolved[i])
    return resolved, count


print('testing', missing_power([-50, -60, -80, 'missing'], 2, 2))
print("Expected result ([-50,-60,-80,-95],3)", '\n')
print('testing', missing_power([-50, -60, -80, -50], 2, 5))
print("Expected result ([-50,-60,-80,-50],0)", '\n')
print('testing', missing_power([-50, -60, -80, 'missing'], 2, 1))
print("Expected result ([-50,-60,-80,-80],2)", '\n')
print('testing', missing_power([-50, -60, -80, -50], 2, 2))
print("Expected result ([-50,-60,-80,-50],0)", '\n')
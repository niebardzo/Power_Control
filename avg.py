def avg(power, quality):
    """
    Function calculates average of n last measurements of power and quality.
    :param power: list of every power measurements
    :param quality: list of every quality measurements
    :return: two element tuple with average power and quality
    """
    sum_pow = 0
    sum_qua = 0
    sum_div = 0
    for i in range(len(power)):
        sum_pow += float(power[i]) * (2**i/2**len(power))
        sum_qua += float(quality[i]) * (2**i / 2**len(power))
        sum_div += (2**i)/(2**len(power))
    avg_pow = sum_pow / sum_div
    avg_qua = sum_qua / sum_div

    return round(avg_pow, 2), round(avg_qua, 2)

# !!!test
print('testing', avg([-66, -78, -63, -75], [1, 2, 1, 2]))
print("Expected result (-71.6, 1.67)", '\n')
print('testing', avg([50, -78, -63, 60], [1, -2, 1, -5]))
print("Expected result (8.13, -2.60)", '\n')
print('testing', avg([-66.224, -78.55, -63.22, -75], [1.55, 6, 1.33, 2]))
print("Expected result (-71.75, 2.32)", '\n')
print('testing', avg([-66, -78, -63, -75, -55, -69], [1, 2, 1, 2, 3, 4]))
print("Expected result (-66.06, 3.19)", '\n')
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
    if len(power) == 0:
        return 0, 0
    for i in range(len(power)):
        sum_pow += float(power[i]) * (2**i/2**len(power))
        sum_qua += float(quality[i]) * (2**i / 2**len(power))
        sum_div += (2**i)/(2**len(power))
    avg_pow = sum_pow / sum_div
    avg_qua = sum_qua / sum_div

    return round(avg_pow, 2), round(avg_qua, 2)

def avg(power, quality):
    """
    Function calculates average of n last measurements of power and quality.
    :param power: list of every power measurements in n power window
    :param quality: list of every quality measurements in n quality window
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

    return avg_pow, avg_qua

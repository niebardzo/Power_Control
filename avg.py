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
    for i in range(len(power)-1):
        sum_pow += int(power[i]) * (i/len(power))
        sum_qua += int(quality[i]) * (i / len(power))
        sum_div += i/len(power)
    avg_pow = sum_pow / sum_div
    avg_qua = sum_qua / sum_div
    return avg_pow, avg_qua

import math


def worker(data, conf):
    """
        This function check several if statements and based on that determines
            what should be done with power, which means it returns if power should be increased (INC),
            decreased (DEC) or not changed at all (NCH). Additionally it returns the value (float) of said change)
        Firstly, it checks quality of signal and based on that follows one of three possible scenarios.
        Once quality scenario is chosen, function checks if signal power should be increased, decreased or not changed
        and apply appropriate value to said change.
    :param data: tuple of two floats
    :param conf: variable input, can be edited
    :return: tuple of two elements, the first of them being of str type and the second of str type if no change
            is applied or of int type if change is applied.
    """

    signal = data[0]
    quality = data[1]
    x = conf['target'] - signal
    if quality < 2.0:
        if signal >= (conf['target'] + conf['hister']):
            action = 'DEC'
            if math.fabs(x) >= conf['maxDec']:
                value = conf['maxDec']
            else:
                value = math.fabs(x)
        elif signal <= (conf['target'] - conf['hister']):
            action = 'INC'
            if x >= conf['maxInc']:
                value = conf['maxInc']
            else:
                value = x
        elif (conf['target'] - conf['changeThresh']) < signal < (conf['target'] + conf['changeThresh']):
            action = 'NCH'
            value = ''
        elif (conf['target'] - conf['hister']) < signal <= (conf['target'] - conf['changeThresh']):
            action = 'INC'
            value = conf['maxIncHist']
        elif (conf['target'] + conf['changeThresh']) <= signal < (conf['target'] + conf['hister']):
            action = 'DEC'
            value = conf['maxDecHist']
    elif 2.0 <= quality < 4:
        if (conf['target'] - conf['changeThresh']) < signal < (conf['target'] + conf['changeThresh']):
            action = 'NCH'
            value = ''
        elif signal <= (conf['target'] - conf['hister']):
            action = 'INC'
            if x >= conf['maxInc']:
                value = conf['maxInc']
            else:
                value = x
        elif (conf['target'] - conf['hister']) < signal <= (conf['target'] - conf['changeThresh']):
            action = 'INC'
            value = conf['maxIncHist']
        elif signal >= (conf['target'] + conf['changeThresh']):
            action = 'NCH'
            value = ''
    elif quality >= 4:
        action = 'INC'
        if signal > (conf['target'] - conf['hister']):
            value = 2.0
        elif signal <= (conf['target'] - conf['hister']):
            if x >= conf['maxInc']:
                value = conf['maxInc']
            else:
                value = x
    if value != '':
        value = round(float(value))
    result = (action, value)
    return result

import math


def worker(data, conf):
    '''
        This function check several if statements and based on that determines
            what should be done with power, which means it returns if power should be increased (INC),
            decreased (DEC) or not changed at all (NCH). Additionally it returns the value (float) of said change)
        Firstly, it checks quality of signal and based on that follow one of three possible scenarios.
        Once quality scenario is chosen, function check if signal power should be increased, decreased or not changed
        and apply appropriate value to said change.

    :param data:
    :param conf:
    :return:
    '''

    signal = data[0]
    quality = data[1]
    x = conf['target'] - signal
    if quality < 2.0:
        if signal > (conf['target'] + conf['hister']):
            if math.fabs(x) >= conf['maxDec']:
                action = 'DEC'
                value = conf['maxDec']
            else:
                action = 'DEC'
                value = x
        elif signal < (conf['target'] - conf['hister']):
            if x >= conf['maxInc']:
                action = 'INC'
                value = conf['maxInc']
            else:
                action = 'INC'
                value = x
        else:
            if (conf['target']-1.0) <= signal <= (conf['target']+1.0):
                action = 'NCH'
                value = ''
            elif signal > conf['target']:
                    action = 'DEC'
                    value = conf['maxDecHist']
            elif signal < conf['target']:
                    action = 'INC'
                    value = conf['maxIncHist']
    elif 2.0 <= quality <= 3.999999:
        if (conf['target']) <= signal <= (conf['target']+1):
            action = 'NCH'
            value = ''
        elif signal < (conf['target'] - conf['hister']):
            if x >= conf['maxInc']:
                action = 'INC'
                value = conf['maxInc']
            else:
                action = 'INC'
                value = x
        elif signal > conf['target']:
            action = 'NCH'
            value = ''
    elif quality >= 4:
        action = 'INC'
        if signal >= (conf['target']-2.0):
            value = 2.0
        elif signal <= (conf['target'] - conf['maxInc']):
            value = conf['maxInc']
        else:
            value = x
    result = (action ,value)
    return result


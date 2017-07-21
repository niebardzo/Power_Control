
def conf_check(conf):
    """Function checks if all the values in conf dictionary are okay.
    Values must be natural numbers. Valid range of values for target is 45-90.
    Also prints information about parameters being updated or not.

    Input = conf dict
    Output = None if everything okay. Exception risen if some parameter
    is invalid"""

    default = {'target': -75,
            'hister': 3,
            'maxInc': 8,
            'maxIncHist': 1,
            'maxDec': 4,
            'maxDecHist': 1,
            'changeThresh': 1,
            'maxMissing': 3,
            'window': 8,
            'offset': 3}

    if conf['target'] < 45 or conf['target'] > 95:
        raise Exception("Invalid parameter")

    for item in conf.keys():
        if conf[item]<0 or not type(conf[item])==int:
            raise Exception("Invalid parameter")


    for item in conf.keys():
        if conf[item]==default[item]:
            print("Value of %s is by default set to %d"%(item, conf[item]))
        else:
            print("Successfully updated %s to value: %d"%(item, conf[item]))

    return

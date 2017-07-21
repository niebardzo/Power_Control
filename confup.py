def conf_read():
    """Input = config file, conf.cfg located in the same directory
    Output = conf dictionary, overriding default configuration"""
    with open('conf.cfg', 'r') as f:
        conf = {'target': -75,
                'hister': 3,
                'maxInc': 8,
                'maxIncHist': 1,
                'maxDec': 4,
                'maxDecHist': 1,
                'changeThresh': 1,
                'maxMissing': 3,
                'window': 8,
                'offset':3}
        while True:
            try:
                conf_line = f.readline().replace('\n', '')
                if conf_line.startswith('#'):
                    pass
                else:
                    conf[conf_line.split(':')[0]] = int(conf_line.split(':')[1])
            except:
                break

    return conf

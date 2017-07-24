import sys


def conf_read():
    """Input = config file, conf.cfg located in the same directory
    Output = conf dictionary, overriding default configuration"""
    default = {'target': -75,
               'hister': 3,
               'maxInc': 8,
               'maxIncHist': 1,
               'maxDec': 4,
               'maxDecHist': 1,
               'changeThresh': 1,
               'maxMissing': 3,
               'window': 8,
               'offset': 3,
               'minAmount': 4}

    if '-c' in sys.argv:
        conf = default.copy()
        print("Loading customized configuration")
        with open('conf.cfg', 'r') as f:
            for line in f:
                if line.startswith('#'):
                    continue
                else:
                    conf[line.split(':')[0]] = int(line.split(':')[1])

        if conf['target'] not in range(-95, -44):
            print("Invalid target parameter, setting target to %s" % (default['target']))
            conf['target'] = default['target']

        if conf['minAmount'] > conf['window']:
            print("Window must be bigger than minimum amount of measurements")
            print("Setting window to %s" % (conf['minAmount']))
            conf['window'] = conf['minAmount']

        for item in conf.keys():
            if item != 'target' and conf[item] < 0:
                print("Invalid value of %s, setting to %s" % (item, default[item]))
                conf[item] = default[item]

        return conf
    else:
        print("Loading default configuration")
        return default

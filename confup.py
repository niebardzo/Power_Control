def confRead():
    with open('conf.cfg', 'r') as f:
        conf={'target': 75,
              'hister': 3,
              'maxInc': 8,
              'maxIncHist': 1,
              'maxDec': 4,
              'maxDecHist': 1,
              'changeThresh': 1,
              'maxMissing': 3,
              'window': 8}
        while True:
            try:
                confLine = f.readline().replace('\n', '')
                if confLine.startswith('#'):
                    pass
                else:
                    conf[confLine.split(':')[0]]= int(confLine.split(':')[1])
            except:
                break


    return conf

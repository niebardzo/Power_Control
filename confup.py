def confRead():
    with open('conf.cfg', 'r') as f:
        conf={}
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
print(confRead())
#try:
#    target = conf['target']
#    maxInc = conf['maxInc']
#    maxIncHist = conf['maxIncHist']
#    window = conf['window']
#    changeThresh = conf['changeThresh']
#    hister = conf['hister']
#    maxDec = conf['maxDec']
#    maxDecHist = conf['maxDecHist']
#    maxMissing = conf['maxMissing']
#except:
#    print("Not valid conf file")

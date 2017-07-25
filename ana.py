import sys


def tcpfilter(file):
    ok200 = 0
    gethttp = 0
    with open(file, 'r'):
        for line in file:
            if ('GET' in str(line)) and ('HTTP' in str(line)):
                gethttp += 1
            elif '200 OK' in str(line):
                ok200 += 1

    print("GET sent %s times" % gethttp)
    print("200 OK response received %s times" % ok200)


tcpfilter(sys.argv[1])

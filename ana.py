import sys


def tcpfilter(file):
    """
    Function filtering tcpdump file to allow us to debug
    communication between our program and server. In this function
    we are filtering line with HTTP GET method and response 200 OK
    :param file: file from tcpdump
    as a result we get print of lines interesting for us.
    """
    ok200 = 0
    gethttp = 0
    with open(file, 'r') as string:
        for line in string:
            if ('GET' in str(line)) and ('HTTP' in str(line)):
                gethttp += 1
            elif '200 OK' in str(line):
                ok200 += 1

    print("GET sent %s times" % gethttp)
    print("200 OK response received %s times" % ok200)


tcpfilter(sys.argv[1])

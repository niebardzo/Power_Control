import sys
import time
from http_request import request

from confup import conf_read
from missing import missing_power
from dbsender import dbsender
from read_file import read_file
from avg import avg
from handover import handover_a
from robol import worker


def pc():
    """Function takes an input file containing measurement data of signal transmission
    and sends back an information about power change. Possible commands:
    INC - Increasing power by specified amount
    DEC - Decreasing power by specified amount
    NCH - Power level is satisfying customer's needs and no action is required
    HOBC - Possibility of handover

    Input = file
    Output = string"""
    start = time.clock()
    conf = conf_read()
    Phones = {}
    count = 0
    pack =[]
    if '-h' in sys.argv:
        print("Handover algorithm initialized")

    for line in sys.stdin:

        try:
            count += 1
            debug("Current input line \t" + line)
            debug("Line number %s\n" % count)
            file_line = read_file(line)
        except ValueError:
            debug("Line incorrect\n")
            continue
        # Checking for input line errors

        debug("Line correct\n")
        phone = file_line[2]
        direction = file_line[0]

        if '-db' in sys.argv:
            if len(pack)<50:
                pack.append(file_line)
            else:
                try:
                    for item in pack:
                        request(item)
                    pack = []
                except:
                    dbsender(pack)       # Sending measurements to database
                    pack = []

        if (phone in Phones) and ('-h' in sys.argv) and len(Phones[phone][direction][0])>=conf['minAmount']:
            do_hand = handover_a(file_line, avg(Phones[phone][direction][0], Phones[phone][direction][1]),
                                 conf['offset'])
            if do_hand == 1:
                pass
            elif do_hand == 2:
                continue
            elif do_hand == 3:
                print('%s\t%s\t%s\tHOBC' % (file_line[0], file_line[1], file_line[2]))
                continue

        else:
            if file_line[1].startswith('N'):
                continue

        # Checking for 'N' starting lines and possibility of Handover

        if phone in Phones:
            Phones[phone][direction][0].append(file_line[3])
            Phones[phone][direction][1].append(file_line[4])
            if len(Phones[phone][direction][0]) > conf["window"]:
                Phones[phone][direction][0].pop(0)
                Phones[phone][direction][1].pop(0)

        else:
            Phones[file_line[2]] = {"UL": [[], [], 0], "DL": [[], [], 0]}
            Phones[phone][direction][0].append(file_line[3])
            Phones[phone][direction][1].append(file_line[4])
        # Updating Phones dictionary with new line

        change_list = missing_power(Phones[phone][direction][0], conf['maxMissing'],
                                    Phones[phone][direction][2])

        debug("Missing power result:  %s %s \n" % (change_list[0], change_list[1]))
        Phones[phone][direction][0] = change_list[0]
        Phones[phone][direction][2] = change_list[1]

        debug("Current power history %s\nCurrent quality history %s"
              "\nConsecutive missings %s\n" % (Phones[phone][direction][0],
                                               Phones[phone][direction][1],
                                               Phones[phone][direction][2]))

        # Checking for missing statements, interpolating measurements when needed

        if len(Phones[phone][direction][0]) >= conf['minAmount']:

            debug("Enough data to take an action\n")
            averages = avg(Phones[phone][direction][0], Phones[phone][direction][1])
            debug("Average power: %s\nAverage quality:%s\n" % (averages[0], averages[1]))
            m_data = worker(averages, conf)

            # Working out command

            print("%s\t%s\t%s\t%s\t%s" % (file_line[0], file_line[1], file_line[2],
                                          m_data[0], m_data[1]))

            debug("Command sent: %s\t%s\t%s\t%s\t%s\n\n" % (file_line[0], file_line[1], file_line[2],
                                                            m_data[0], m_data[1]))
            # Printing out command
        else:
            print("%s\t%s\t%s\t%s" % (file_line[0], file_line[1], file_line[2], 'NCH'))
            debug("Not enough data\n\n")

    if '-db' in sys.argv:
        try:
            for item in pack:
                request(item)
        except:
            dbsender(pack)  # Sending measurements to database
    end = time.clock()
    print("Finished in", (end-start))
    return


def debug(something):
    """Function sends information to logdeb.txt file"""

    if '-d' in sys.argv:
        with open('logdeb.txt', 'a') as f:
            f.write(something)

pc()

import time
import sys
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

    conf = conf_read()
    send_pack = []
    Phones = {}
    for line in sys.stdin:
        time.sleep(0.5)
        try:
            file_line = read_file(line)
        except ValueError:
            continue
        # Checking for input line errors

        phone = file_line[2]
        direction = file_line[0]

        if len(send_pack)<10:
            send_pack.append(file_line)
        else:
            dbsender(send_pack)  # Sending measuremens to database
            send_pack = []

        if (phone in Phones) and ('-h' in sys.argv):
            do_hand = handover_a(file_line, avg(Phones[phone][direction][0], Phones[phone][direction][1]),
                                 conf['offset'], conf['target'])
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

        change_list = missing_power(Phones[phone][direction][0],
                                    Phones[phone][direction][2], conf["maxMissing"])
        Phones[phone][direction][0] = change_list[0]
        Phones[phone][direction][2] = change_list[1]

        # Checking for missing statements, interpolating measurements when needed
        m_data = worker(avg(Phones[phone][direction][0], Phones[phone][direction][1]), conf)

        # Working out command

        print("%s\t%s\t%s\t%s\t%s" % (file_line[0], file_line[1], file_line[2],
                                      m_data[0], m_data[1]))

        # Printing out command

    return


pc()

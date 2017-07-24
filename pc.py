import time
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

    Phones = {}
    count = 0
    while True:
        time.sleep(0.5)
        count += 1
        try:
            file_line = read_file()
        except ValueError:
            continue
        except EOFError:
            break
        # Checking for input line errors

        phone = file_line[2]
        direction = file_line[0]

        dbsender(file_line)  # Sending measurement line to database
        # try:
        #     do_hand = handover_a(file_line, avg(Phones[phone][direction][0],Phones[phone][direction][1]),
        #                      conf['offset'], conf['target'])
        # except KeyError:
        #     print("Here 1.5")
        #     continue
        #
        # if do_hand == 1:
        #     print("here2")
        #     pass
        # elif do_hand == 2:
        #     continue
        # elif do_hand == 3:
        #     print('%s\t%s\t%s\tHOBC' % (file_line[0], file_line[1], file_line[2]))
        #     continue

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
        print(m_data)
        print(Phones[phone][direction][0], Phones[phone][direction][1], avg(Phones[phone][direction][0], Phones[phone][direction][1]))
        # Working out command
        print("%s\t%s\t%s\t%s\t%s" % (file_line[0], file_line[1], file_line[2],
                                      m_data[0], m_data[1]))

        print(count)
        # Printing out command

    return


pc()

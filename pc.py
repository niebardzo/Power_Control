from confup import conf_read
from confcheck import conf_check


def pc():
    """Function takes an input file containing measurement data of signal transmission
    and sends back an information about power change. Possible commands:
    INC - Increasing power by specified ammount
    DEC - Decreasing power by specified ammount
    NCH - Power level is satisfying customer's needs and no action is required

    Input = file
    Output = string"""

    conf = conf_read()

    try:
        conf_check(conf)
    except:
        print("Invalid parameteres. Loading default configuration")
        conf = {'target': 75,
                'hister': 3,
                'maxInc': 8,
                'maxIncHist': 1,
                'maxDec': 4,
                'maxDecHist': 1,
                'changeThresh': 1,
                'maxMissing': 3,
                'window': 8}

    Phones = {}

    while True:
        try:
            file_line = read_file()
        except EOFError:
            break
        except ValueError:
            continue

        phone = file_line[2]
        direction = file_line[0]

        handover_a(file_line)

        if phone in Phones:
            Phones[phone][direction][0].append(file_line[3])
            Phones[phone][direction][1].append(file_line[4])
            if len(Phones[phone][direction][0]) > conf["window"]:
                Phones[phone][direction][0].pop(0)
                Phones[phone][direction][1].pop(0)

        else:
            Phones[file_line[2]] = {"UL": [[], []], "DL": [[], []]}
            Phones[phone][direction][0].append(file_line[3])
            Phones[phone][direction][1].append(file_line[4])

        m_data = worker(avg(Phones[phone][direction][0],Phones[phone][direction][1]))

        dbsender("%s\t%s\t%s\t%s\t%s" % (file_line[0], file_line[1], file_line[2],
                                        m_data[0], m_data[1]))

    return


pc()

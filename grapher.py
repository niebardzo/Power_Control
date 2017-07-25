import sqlite3
import matplotlib.pyplot as plt
import sys


def db_read(start, end, ms):
    """Function connects to database with measurements history and fetch data from it,
    data is initially filtered by SQL querry and then filtered again, due to python3
    well implemented string comparison
    Input:
    start - beginning of time window
    end - end of time window
    ms - mobile station alias

    Output = graphical representation of measurements"""
    conn = sqlite3.connect("measure_hist.db")
    c = conn.cursor()
    c.execute("SELECT Direction, Power, Time FROM HISTORY "
              "WHERE (Mobile = '%s') AND (Transmiter = 'S0') " % ms)
    data = c.fetchall()

    DL = []
    UL = []

    for item in data:
        if start < item[2] < end:
            if item[0] == 'UL' and item[1] != 'missing':
                UL.append(item[1])

            elif item[0] == 'DL' and item[1] != 'missing':
                DL.append(item[1])

    plt.title("UL and DL power for %s" % ms)
    plt.plot(UL, label='UL')
    plt.plot(DL, label='DL')
    plt.legend()
    plt.xlabel('Measurement no.')
    plt.ylabel('Power [dBm]')
    plt.show()


db_read(sys.argv[1], sys.argv[2], sys.argv[3])

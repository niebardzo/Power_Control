import sqlite3


def dbsender(pack):
    """Function is creating table in "measure_hist.db" database,
    located in the same directory. If table exists, adds next row of measurements"""

    conn = sqlite3.connect("measure_hist.db")
    c = conn.cursor()
    for line in pack:
        c.execute('''CREATE TABLE IF NOT EXISTS HISTORY 
            (Direction text, Transmiter text, Mobile text, Power text, Quality text)''')
        c.execute("INSERT INTO HISTORY VALUES (?, ?, ?, ?, ?)", line)
    conn.commit()


#dbsender(["DL", "S0","MS226","-60","4"])
import sys


def read_file():
    """
    Function reads the input signal data and filters it to check if given input lines are valid.
    If some element in read line is invalid, the function will raise an Error
    :return: single list of strings from one line read from standard input
    """

    parameter_list = ['' for _ in range(5)]
    input_data = sys.stdin.readline()

    if input_data:
        print(input_data, parameter_list)
        parameter = input_data.split()

        for _ in range(len(parameter)):
            parameter_list[_] = parameter[_]

        dl_ul = parameter_list[0]
        bts = parameter_list[1]
        ms = parameter_list[2]
        signal_strength = parameter_list[3]
        signal_quality = parameter_list[4]

        # checking if DL/UL
        if dl_ul != ('DL' or 'UL'):
            raise ValueError("Invalid data")

        # checking BTS validity
        bts_list = ['S0', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6']
        if bts not in bts_list:
            raise ValueError("Invalid BTS")

        for _ in ms:
            if _ not in "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM":
                raise ValueError("Invalid MS")

        if signal_strength == 'missing':
            pass
        elif int(signal_strength) not in range(-95, -44):
            raise ValueError("Signal strength out of range")

        if signal_quality == '':
            parameter_list[4] = '5'

        print(parameter_list)

        return parameter_list

    else:
        raise EOFError

read_file()


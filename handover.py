from math import fabs


def handover_a(f_line, avg_power, hister, target):
    """
    Function which does the following things:
    - compares power measurement of current cell to another cell
    - recommends handover
    :param f_line: list of strings from input
    :param avg_power: avg power of current cell
    :param hister: minimum offset before handover
    :param target: power target
    :return: string
    """
    cell = f_line[1]
    if cell == 'S0':
        return 1
    else:
        dist_s0 = abs(avg_power) + abs(hister) - abs(target)
        dist_nx = abs(target) - abs(float(f_line[3]))
        if fabs(dist_nx) < fabs(dist_s0):
            return 3
        else:
            return 2

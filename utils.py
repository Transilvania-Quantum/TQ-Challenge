# Constants

VELOCITY = 1  # 1 KM/min

PC_KM = 0.02  # % of battery/KM


def calculate_time_cost(inp, order, charge):
    """

    :param inp: [[float, ],..] nxn input  matrix n= nr of stations
    :param order: [ int ,...] order in witch the stations need to be visited
    :param charge: [float, ...] percentage that need to be charge at each station (0-1)
    :return: float , time required to visit all the stations
    """
    time = 0
    for i in range(len(order) - 1):
        time = time + inp[order[i]][order[i + 1]]
        time = time + charge[i] * inp[i][i]

    return time


def battery_check(inp, order, charge):
    """
    :param inp: [[float, ],..] nxn input  matrix n= nr of stations
    :param order: [ int ,...] order in witch the stations need to be visited
    :param charge: [float, ...] percentage that need to be charge at each station (0-1)
    :return: 0 if the battery is well charged 1 otherwise
    """
    battery = 1
    for i in range(len(order) - 1):
        battery = battery - inp[order[i]][order[i + 1]] * PC_KM
        if battery < 0.0:
            return 1
        battery = battery + charge[i + 1]

    return 0


def order_check(order, inp):
    """

    :param order: [ int ,...] order in witch the stations need to be visited
    :param inp: [[float, ],..] nxn input  matrix n= nr of stations
    :return: o if the order is valid 0 otherwise
    """
    for i in range(len(order)):
        if i not in order:
            return 1

    if len(order) != len(inp):
        return 1

    return 0


def evaluate(inp, order, charge):
    """

    :param inp: [[float, ],..] nxn input  matrix n= nr of stations
    :param order: [ int ,...] order in witch the stations need to be visited
    :param charge: [float, ...] percentage that need to be charge at each station (0-1)
    :return: time if the solution is valid.
    """

    if battery_check(inp, order, charge) != 0:
        return "You don't have a valid charging scheme."

    if order_check(order, inp) != 0:
        return "Invalid order."

    return calculate_time_cost(inp, order, charge)

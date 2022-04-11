from utils import *


###
# Your code
###



def build_solution(inp):
    """

    :param inp:
    :return:
    """
    order = [i for i in range(len(inp))]
    charge = [0 for 0 in range(len(order))]

    ###
    # Your code
    ###

    time = evaluate(inp, order, charge)

    return order, charge, time

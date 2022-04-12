from test_input import *
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
    charge = [0.02 for i in range(len(order))]

    ###
    # Your code
    ###

    return order, charge, evaluate(inp, order, charge)


###

time = 0
for key in TEST:
    _, _, timex = build_solution(TEST[key])
    if isinstance(timex, str):
        print("Invalid order or charge")
    else:
        print("{} time", time)
        time = time+timex

print("Total time", time)

###
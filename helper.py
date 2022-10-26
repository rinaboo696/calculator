import consts

def to_number(candidate):
    try:
        return float(candidate)
    except:
        raise TypeError(consts.TO_NUMBER_ERROR_MESSAGE)
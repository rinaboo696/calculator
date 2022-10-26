import sys
import consts
import helper

def try_input(message):
     candidate = input(message)
     if candidate == consts.ESCAPE:
        sys.exit()
     else:
        return candidate 

def try_input_number(message):
    candidate = try_input(message)
    if len(candidate) > 9:
        print("Warning! The number is too long. The number was cut.")
        candidate = candidate[0:9]
        print(candidate)
    try:
        return helper.to_number(candidate)
    except Exception as error:
        print(error)
        return try_input_number(message)

def try_input_operator(message):
    candidate = try_input(message)
   
    if candidate == consts.PLUS or candidate == consts.MINUS or candidate == consts.MULTIPLICATION or candidate == consts.SEPARATOR:
        return candidate
    else:
        print(consts.TO_OPERATOR_ERROR_MESSAGE)
        return try_input_operator(message)
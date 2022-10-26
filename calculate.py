import consts
import operations

def calculate(operator, first_value, second_value):
    match operator:
        case consts.PLUS:
            return operations.sum(first_value, second_value)
        case consts.MINUS:
            return operations.sub(first_value, second_value)
        case consts.MULTIPLICATION:
            return operations.mult(first_value, second_value)  
        case consts.SEPARATOR:  
            return operations.div(first_value, second_value) 
        case _:
            raise TypeError(consts.MATCH_OPERATOR_ERROR_MESSAGE)
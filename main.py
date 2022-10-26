import consts
import inputs
import calculate


print("If you want to escape , press " + consts.ESCAPE)

result = inputs.try_input_number("input first value: ")

while True:
    operator = inputs.try_input_operator("what we are going to do?: ")
    next_value = inputs.try_input_number("input value: ")
    result = calculate.calculate(operator, result, next_value)
    print(result)




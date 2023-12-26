from random import randint

from constants import ArithmeticOperations


def generate_math_exercises(count, arithmetic_operation=''):
    for i in range(count):
        if arithmetic_operation == ArithmeticOperations.SUBTRACTION:
            minuend, subtrahend = generate_exercise_parts(is_for_subtraction=True)
            print(f'{i}. {minuend}-{subtrahend} = ')
        elif arithmetic_operation == ArithmeticOperations.ADDITION:
            addedn_1, addedn_2 = generate_exercise_parts()
            print(f'{i}. {addedn_1}+{addedn_2} = ')
        elif arithmetic_operation == ArithmeticOperations.MULTIPLICATION:
            multiplier,multiplicant = generate_exercise_parts()
            print(f'{i}. {multiplier}*{multiplicant} = ')
        elif arithmetic_operation == ArithmeticOperations.DIVISION:
            dividend, divisor = generate_division_parts()
            print(f'{i}. {dividend}:{divisor} = ')


def generate_division_parts():
    dividend, divisor = generate_exercise_parts()
    # division without ending
    while (dividend < divisor) or (dividend % divisor != 0):
        dividend, divisor = generate_exercise_parts()
    return dividend, divisor


def generate_exercise_parts(is_for_subtraction=False):
    part_1 = randint(100, 999)
    part_2 = randint(100, 999)
    if is_for_subtraction:
        while part_2 > part_1:
            part_2 = randint(100, 999)
    return part_1, part_2


generate_math_exercises(100, ArithmeticOperations.DIVISION)

from random import randint

from constants import ArithmeticOperations


def generate_math_exercises(count, arithmetic_operation=''):
    for i in range(count):
        if arithmetic_operation == ArithmeticOperations.SUBTRACTION:
            minuend, subtrahend = generate_exercise_parts(is_for_subtraction=True)
            print(f'{i}. {minuend}-{subtrahend} = ')
        elif arithmetic_operation == ArithmeticOperations.ADDITION:
            addedn_1, addend_2 = generate_exercise_parts()
            print(f'{i}. {addedn_1}+{addend_2} = ')
        else:
            print(f'here is a room for an improvement')
            break


def generate_exercise_parts(is_for_subtraction=False):
    part_1 = randint(100, 999)
    part_2 = randint(100, 999)
    if is_for_subtraction:
        while part_2 > part_1:
            part_2 = randint(100, 999)
    return part_1, part_2


generate_math_exercises(5, ArithmeticOperations.SUBTRACTION)

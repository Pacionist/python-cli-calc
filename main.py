import math
import sys

math_input = input().split(" ")


def calc(math_eq: list):
    if math_eq.__len__() != 3:
        sys.stderr.write("Вы ввели не выражение!")
        sys.exit(1)
    eq: Equation = Equation(math_eq)
    print(eq.calculate())


class Equation:
    def __init__(self, eq: list):
        try:
            self.number_first: int = int(eq[0])
            self.number_second: int = int(eq[2])
        except ValueError as e:
            sys.stderr.write("Вы неверно ввели число!")
            sys.exit(1)
        self.operation = eq[1]

    def calculate(self) -> int:
        match self.operation:
            case "+": return self.number_first + self.number_second
            case "-": return self.number_first - self.number_second
            case "*": return self.number_first * self.number_second
            case "/":
                if self.number_second == 0:
                    sys.stderr.write("На ноль делить нельзя!")
                    sys.exit(1)
                return math.ceil(self.number_first / self.number_second)
            case _:
                sys.stderr.write("Вы неверно ввели операцию!")
                sys.exit(1)


calc(math_input)

import random

import src.calculator as c

TEST_NUM = 10

calc = c.Calculator()

for _ in range(10):
    a, b, op = random.randint(0, 10), random.randint(0, 10), \
        random.choice(calc.OPERATORS)
    expr = f"{a}{op}{b}"

    assert eval(expr) == calc.parse(expr), f"Failed on: {expr}"

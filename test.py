from typing import Literal

op1: Literal[3] = 3
op2: Literal[4] = 4
c = op1 + op2
reveal_type(c)


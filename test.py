from z3 import *

x, y = Int('x'), Int('y')

s = Solver()

s.add(x + 2 * y > 4)
s.add(3 * x - y == 3)

s.check()
print(s.model())


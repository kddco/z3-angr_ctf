from z3 import *
x = BitVec('x',16)
print(is_bv(x))
print(x.size())
print(x.sort())
word = BitVecSort(16)
x2 = BitVec('x',word)
print(eq(x,x2))


# need to edit this every time I add a new solution
from time import time

# solution to https://projecteuler.net/problem=32
from solutions import PandigitalProducts32 
start_time = time.time()

def test_problem_32():
  print(pandigitalSum("123456789"))
  
print("pandigitalSum finished in --- %s seconds ---" % (time() - start_time))
    

import array as arr
from random import shuffle
import sys

# lists
list_1 = [10, "Chelsea", 20]

# Tuples
tup_1 = (10, "Chelsea", 20)

# Arrays
My_Array=arr.array('i',[1,2,3,4])
# reverse the order
My_Array[::-1]

x = ['Keep', 'The', 'Blue', 'Flag', 'Flying', 'High']
shuffle(x)

x = list(range(1,10000))
print (type(x))

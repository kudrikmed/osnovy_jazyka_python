from itertools import count
from itertools import cycle


for i in count(3):
    if i < 11:
        print(i)
    else:
        break

counter = 0
for i in cycle([1, 2, 3]):
    if counter < 15:
        print(i)
        counter += 1
    else:
        break

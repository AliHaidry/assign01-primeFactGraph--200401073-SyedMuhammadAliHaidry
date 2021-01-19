# Finding Prime numbers between given intervals


import time
import matplotlib.pyplot as plt
import numpy as np

LowerBound = int(input("input the lower value:   "))
UpperBound = int(input("input the upper value:    "))

start = time.time()

prime = []
timeTracker = []
for priNum in range(LowerBound, UpperBound + 1):
    # all prime numbers are greater than 1
    if priNum > 1:
        for i in range(2, priNum):
            if (priNum % i) == 0:
                break
        else:
            prime.append(priNum)
            timeTracker.append((time.time() - start))

print("The generated prime numbers in given interval are:", prime)

# ploting the prime values and according to their discovering time
plt.plot(timeTracker, prime, color='tab:red')
plt.ylabel('Prime Number')
plt.xlabel('Time Taken')
plt.show()

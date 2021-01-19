
import time
import matplotlib.pyplot as plt


LowerBound = int(input("Enter lower range value:   "))
UpperBound = int(input("Enter upper range value:    "))

start = time.time()

prime = []
timeTracker = []
for priNum in range(LowerBound, UpperBound + 1):
    # prime numbers greater > 1
    if priNum > 1:
        for i in range(2, priNum):
            if (priNum % i) == 0:
                break
        else:
            prime.append(priNum)
            timeTracker.append((time.time() - start))

print("The generated prime numbers in given interval are:", prime)

# plotting prime values with their discovering time
plt.plot(timeTracker, prime, color='tab:red')
plt.ylabel('Prime Number')
plt.xlabel('Time Taken')
plt.show()

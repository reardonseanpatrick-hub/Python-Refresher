# plot.py

import matplotlib.pyplot as plt
from fib import timings

x = list(range(len(timings)))
y = timings

plt.plot(x, y)
plt.xlabel("n (Fibonacci number)")
plt.ylabel("Time (seconds)")
plt.title("Execution Time of Recursive Fibonacci")
plt.grid(True)

plt.savefig("fib_timing.png")
plt.show()

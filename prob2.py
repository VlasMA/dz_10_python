#Диаграмма рассеяния (точечная)

import matplotlib.pyplot as plt
import random

f = lambda x: random.randint(1, 10)

x = list(map(f, range(1, 10)))
y = list(map(f, range(1, 10)))

print(x)
print(y)

plt.plot(x, y, 'ro')
plt.show()




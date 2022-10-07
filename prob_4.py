# Создание круговой диаграммы (ghjlf;b pf gthdjt gjkeujlbt)

import matplotlib.pyplot as plt
# Data to plot
month = 'янв', 'фев', 'мар', 'апр', 'май', 'июнь'
speed = [8, 7, 12, 4, 3, 2]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'red', 'blue']
explode = (0, 0, 0, 0, 0, 0) # explode 1st slice

# Plot
plt.pie(speed, explode=explode, labels=month, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.show()



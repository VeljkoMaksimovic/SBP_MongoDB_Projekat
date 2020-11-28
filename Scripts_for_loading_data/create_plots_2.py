import numpy as np
import matplotlib.pyplot as plt

N = 12
v2 = (23679, 23679, 22467, 23679, 23679, 22467, 23679, 21816, 23679, 22467, 21816, 21816)

ind = np.arange(12)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
rects2 = ax.bar(ind, v2, width, color='r')
v3 = (23679, 23679, 22467, 6323, 6323, 22467, 23679, 21816, 23679, 2401, 21816, 21816)
rects3 = ax.bar(ind + width, v3, width, color='b')
# add some text for labels, title and axes ticks
ax.set_ylabel('ms')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(('1', '2', '3', '4.1', '4.2', '5', '6', '7', '8', '9', '10.1', '10.2', ))

ax.legend((rects2[0], rects3[0]), ('v2', 'v3'))


def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')


#autolabel(rects2)
#autolabel(rects3)

avg_diff = 0
for i in range(len(v2)):
    avg_diff += (v2[i]/v3[i])
print(avg_diff/12)
plt.savefig('v1_and_v2_and_v3.png')
plt.show()

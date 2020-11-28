import numpy as np
import matplotlib.pyplot as plt

N = 12
v1 = (94, 102, 150, 130, 124, 148, 173, 96, 143, 135, 109, 134)

ind = np.arange(12)  # the x locations for the groups
width = 0.30       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind-width/2, v1, width, color='r')

v2 = (42, 54, 84, 35, 27, 168, 100, 39, 31, 22, 55, 49)
rects2 = ax.bar(ind+width/2, v2, width, color='y')

v3 = (39, 46, 78, 20, 21, 158, 93, 41, 33, 14, 39, 41)
rects3 = ax.bar(ind + 1.5*width, v3, width, color='b')
# add some text for labels, title and axes ticks
ax.set_ylabel('ms')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(('1', '2', '3', '4.1', '4.2', '5', '6', '7', '8', '9', '10.1', '10.2', ))

ax.legend((rects1[0], rects2[0], rects3[0]), ('v1', 'v2', 'v3'))


def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

avg_diff = 0
for i in range(len(v1)):
    avg_diff += (v1[i]/v2[i])
print(avg_diff/12)
plt.savefig('v1_and_v2_and_v3.png')
plt.show()

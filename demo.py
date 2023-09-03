import numpy as np
import matplotlib.pyplot as plt
Run = [[3,15,35,30],[5,28,59,37],[7,24,49,29]]
x = np.arange(4)
plt.bar(x+0.00,Run[0],color='c',width=0.20)
plt.bar(x+0.25,Run[1],color='m',width=0.20)
plt.bar(x+0.5,Run[2],color='k',width=0.20)
plt.show()
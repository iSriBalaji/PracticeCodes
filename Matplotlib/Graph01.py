import numpy as np
import matplotlib.pyplot as plt
data = [[30, 25, 50, 20],
[40, 23, 51, 17],
[35, 22, 45, 19]]
X = np.arange(4)
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(X + 0.00, data[0], color = 'b',label="11111", width = 0.25)
ax.bar(X + 0.25, data[1], color = 'g',label="22222", width = 0.25)
ax.bar(X + 0.50, data[2], color = 'r',label="33333", width = 0.25)
plt.legend()
plt.show()

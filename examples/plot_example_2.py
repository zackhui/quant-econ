import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()
x = np.linspace(0, 10, 200)
y = np.sin(x)
ax.plot(x, y, 'r-', lw=2, label='sine function', alpha=0.6)
ax.legend(loc='upper center')
plt.show()

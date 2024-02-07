from fortpy import sine_grid
import matplotlib.pyplot as plt

ds = sine_grid()
ds['data'].plot()
plt.show()

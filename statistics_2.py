from matplotlib import pyplot as plt
import numpy as np
from scipy.stats import norm

plt.figure(figsize=(10, 10))

plt.text(0.01, 0.9, "Как мы увидим из представленных далее графиков,", fontsize=20)
plt.text(0.01, 0.8, "при изменении математического ожидания наш", fontsize=20)
plt.text(0.01, 0.7, "график не изменяет формы, а смещается, а при", fontsize=20)
plt.text(0.01, 0.6, "увеличении дисперсии видим, что график", fontsize=20)
plt.text(0.01, 0.5, "становится площе то есть данные приближены к", fontsize=20)
plt.text(0.01, 0.4, "математическому ожиданию.", fontsize=20)

fig = plt.gca()
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)
plt.show()

x = np.arange (-5, 5, 0.001)
plt.plot (x, norm.pdf(x, 0, 1), label='μ: 0, σ: 1')
plt.plot (x, norm.pdf(x, 1, 1.5), label='μ:1, σ: 1.5')
plt.plot (x, norm.pdf(x, 2, 2), label='μ:2, σ: 2')

plt.legend()

plt.show()
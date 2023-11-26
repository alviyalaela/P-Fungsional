import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

tinggi_badan = [165, 170, 155, 172, 180, 160, 175, 165, 185, 175, 170, 160]
interval_size = 10

plt.hist(tinggi_badan, bins=range(150, 199, interval_size), density=True)

mean_tinggi = np.mean(tinggi_badan)
std_tinggi = np.std(tinggi_badan)

x = np.linspace(min(tinggi_badan), max(tinggi_badan), 100)
plt.plot(x, norm.pdf(x, mean_tinggi, std_tinggi), 'k', label='PDF', linewidth=2,  color="orange")

plt.xlabel('Tinggi Badan')
plt.ylabel('Frekuensi')
plt.title('Histogram Tinggi Badan')

plt.legend()
plt.show()
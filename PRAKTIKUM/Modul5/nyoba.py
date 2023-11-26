import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

def group_heights(heights, interval_size):
    # Menghitung batas interval
    min_height = min(heights)
    max_height = max(heights)
    bins = range(min_height - min_height % interval_size, max_height + interval_size, interval_size)

    # Mengelompokkan tinggi badan ke dalam interval
    grouped_heights = {}
    for height in heights:
        bin_label = (height // interval_size) * interval_size
        if bin_label not in grouped_heights:
            grouped_heights[bin_label] = []
        grouped_heights[bin_label].append(height)

    return bins, grouped_heights

def plot_grouped_histogram(bins, grouped_heights):
    # Menghitung frekuensi di setiap bin
    frequencies = [len(grouped_heights.get(bin_label, [])) for bin_label in bins]

    # Membuat histogram
    plt.hist(frequencies, bins= 10, density=True)

    # Menambahkan kurva PDF
    mean_height = np.mean(tinggi_badan)
    std_height = np.std(tinggi_badan)
    x = np.linspace(min(tinggi_badan), max(tinggi_badan), 100)
    pdf_values = norm.pdf(x, mean_height, std_height)
    plt.plot(x, pdf_values * len(tinggi_badan), 'k', label='PDF', linewidth=2, color="orange")

    # Menambahkan label dan judul
    plt.xlabel('Tinggi Badan')
    plt.ylabel('Frekuensi / Densitas Probabilitas')
    plt.title('Histogram dan Kurva PDF Tinggi Badan')


    # Menampilkan legenda
    plt.legend()

    # Menampilkan histogram
    plt.show()

# Contoh penggunaan fungsi
tinggi_badan = [165, 170, 155, 172, 180, 160, 175, 165, 185, 175, 170, 160]
interval_size = 10
bins, grouped_heights = group_heights(tinggi_badan, interval_size)
plot_grouped_histogram(bins, grouped_heights)

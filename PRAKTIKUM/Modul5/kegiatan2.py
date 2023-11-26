import matplotlib.pyplot as plt
import numpy as np

data_transaksi = [
    ("Produk A", 50, 10),
    ("Produk B", 30, 25),
    ("Produk C", 20, 30),
    ("Produk D", 60, 8),
    ("Produk E", 40, 15),
    ("Produk F", 70, 5),
]

nama_produk, harga_produk, jumlah_terjual = zip(*data_transaksi)
pendapatan_produk = np.array(harga_produk) * np.array(jumlah_terjual)

print("Nama Produk:", nama_produk)
print("Harga Produk:", harga_produk)
print("Jumlah Terjual:", jumlah_terjual)

plt.subplot(1, 2, 1)
plt.title("Hubungan Harga Produk dan Jumlah Produk Terjual")
plt.scatter(harga_produk, jumlah_terjual)
plt.xlabel("Harga Produk")
plt.ylabel("Jumlah Produk Terjual")

plt.subplot(1, 2, 2)
plt.title("Pendapatan Produk")
plt.bar(nama_produk, pendapatan_produk)
plt.xlabel("Nama Produk")
plt.ylabel("Pendapatan Produk")

plt.show()

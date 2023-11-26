from functools import reduce
import matplotlib.pyplot as plt

nilai_mahasiswa = [75, 80, 90, 65, 70, 85, 95, 78, 88, 92]
mahasiswa = list(map(lambda i: f"M{i+1}", range(len(nilai_mahasiswa))))

def hitung_rata_rata(nilai_mahasiswa):
    total_nilai = reduce(lambda x, y: x + y, nilai_mahasiswa)
    average = total_nilai / len(nilai_mahasiswa)
    return average

averageGrade = hitung_rata_rata(nilai_mahasiswa)

print("Mahasiswa:", mahasiswa)
print("Nilai mahasiswa:", nilai_mahasiswa)
print("Rata-rata nilai mahasiswa:", averageGrade)

plt.axhline(y=averageGrade, color='red', linestyle='dashed', linewidth=2, label='Rata-rata')
plt.plot(averageGrade, label='Rata-rata')
plt.xlabel(" Mahasiswa")
plt.ylabel("Nilai Ujian")
plt.bar(mahasiswa, nilai_mahasiswa, color='lightblue')
plt.show()

dictNilai = {}
# Fungsi nilai akhir
def perhitunganNilai(nama, uas, uts):
    nilai = (uas+uts)/2
    dictNilai[nama] = nilai
    
#Fungsi nilai akhir semua mahasiswa
def tampilNilai():
    for x, y in dictNilai.items():
        print("Nama: {}\t Nilai Akhir: {}".format(x,y))

def main():
    dataMahasiswa = {
        "Alviya" : [70,65],
        "Laela" : [80, 90],
        "Rafli" : [0,0]
    }
    for nama, nilai in dataMahasiswa.items():
        perhitunganNilai(nama, nilai[0], nilai[1])

    tampilNilai()

if __name__ == "__main__":
    main()

book_database = {}

def add_book():
    kode_buku = input("Masukkan Kode Buku: ")
    title = input("Masukkan Judul Buku: ")
    writer = input("Masukkan Penulis Buku: ")

    # Fungsi ini bersifat murni, mengembalikan dictionary baru
    def create_book_entry(kode_buku, title, writer):
        return {'Kode Buku': kode_buku, 'Judul': title, 'Penulis': writer}

    book_entry = create_book_entry(kode_buku, title, writer)
    book_database[kode_buku] = book_entry
    print("Buku berhasil ditambahkan!")

def list_books():
    if not book_database:
        print("Buku Kosong!")
    else:
        print("\n[LIST BUKU]\n")
        for kode_buku, book_entry in book_database.items():
            print("Kode Buku:", book_entry['Kode Buku'])
            print("Judul:", book_entry['Judul'])
            print("Penulis:", book_entry['Penulis'])
            print("\n")

def main():
    while True:
        print("Welcome to UMM Library!")
        print("1. Tambah Buku")
        print("2. Lihat List Buku")
        print("3. Keluar")

        choice = input("Pilih menu: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            list_books()
        elif choice == '3':
            print("Terima kasih, sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang benar.")

if __name__ == "__main__":
    main()

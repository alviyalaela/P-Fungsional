# book1 = {
#     'judul' : 'title',
#     'penulis' : 'writer',
# }

# book2 = {
#     'judul' : 'title',
#     'penulis' : 'writer',
# }



book_database = {}
innerDict = {}
borrowed = {}
taker = {}
addbooks = {
    'bookcode' : 'kode_buku',
    'judul' : 'title',
    'penulis' : 'writer'
}

useradm_database = {'alviyes': 'bismillah'}
def booklist():
    if not book_database:
        print("Buku Kosong!")
        login_mhs()
    else:
        print("\n[LIST BUKU]\n")
        for outer1, inner1 in book_database.items():
            # outer1 adalah key dan inner1 adalah value dari book database, jadi maksudnya adalah dictionary dalam dictionary atau nested dictionary
            # outer1 itu untuk kode buku, inner1 untuk judul dan penulis
            print('Kode Buku\t:', outer1)
            for key, value in inner1.items(): # di sini ngeprint value dari key inner1, yaitu judul dan penulis
                print(key, value)
                
def addbooks():
    kode_buku = input("Masukkan Kode Buku: ")
    title = input("Masukkan Judul Buku: ")
    writer = input("Masukkan Penulis Buku: ")
    #setelah itu, inputan dimasukkan ke dictionary innerDict (dictionary smentara), yang punya pasangan key : value seperti di bawah
    innerDict = {
        'Judul\t\t:' : title,
        'Penulis\t\t:' : writer
    }
    
    # lalu inputan dari innerDict masuk ke book database
    book_database[kode_buku] = innerDict

    print("Buku berhasil ditambahkan!")
    print("Tambahkan buku lagi?")
    print("1. Ya")
    print("2. Tidak")        
    pilih = input("Masukkan pilihan: ")
    if pilih == '1':
        addbooks()
    elif pilih == '2':
        print("\n")
        main() 

def borrowbook():
    name = input("Masukkan Nama Mahasiswa: ")
    nim = input("Masukkan NIM Mahasiswa: ")
    kodebuku = input("Masukkan Kode Buku: ")
    innerDict = {
        'name' : name,
        'nim' : nim
    }

    if kodebuku in book_database:
        #buku yang mau dipinjam masuk ke borrowed. terus dihapus di book database, terus masuk ke taker / peminjam
        borrowed[kodebuku] = book_database[kodebuku]
        del book_database[kodebuku]
        taker[kodebuku] = innerDict
            
        print(f"Anda berhasil meminjam buku dengan ID {kodebuku}!")
        login_mhs()

    elif kodebuku in borrowed:
        print(f"Buku dengan ID {kodebuku} telah dipinjam oleh {taker[kodebuku]['name']}.")
        other = input(str("Ingin pinjam buku lain? (Y/N)"))
        if other == 'y' or other == 'Y':
            borrowbook()
        else: 
            login_mhs()

    else:
        print("Buku tidak ditemukan")

def returnbook():
    kodebuku = input("Masukkan kode buku yang akan dikembalikan: ")
    book_database[kodebuku] = borrowed[kodebuku]
    del borrowed[kodebuku]
    del taker[kodebuku]

    print(f"Buku dengan ID {kodebuku} telah berhasil dikembalikan")
    login_mhs()

    
def login_adm():
    uname_adm = input("Username Admin: ")
    pwd_adm = input("Password Admin: ")

    if uname_adm in useradm_database and useradm_database[uname_adm] == pwd_adm:
        print("\nSELAMAT DATANG DI PERPUSTAKAAN UMM")
        addbooks()
        booklist()
    else:
        print("Login gagal. Periksa username dan password Anda.")

def login_mhs():
    print("SELAMAT DATANG DI PERPUSTAKAAN UMM")
    print("What do you need?")
    print("1. Lihat List Buku")
    print("2. Pinjam Buku")
    print("3. Kembalikan Buku")
    print("4. Keluar")
    choose = input("Masukkan pilihan: ")

    if choose == '1':
        booklist()
        print("\n")
        login_mhs()
        
    if choose == '2':
        borrowbook()

    elif choose == '3':
        returnbook()

    elif choose == '4':
        main()
        
def main():
    while True:
        print("Welcome to UMM Library!")
        print("1. Login as admin")
        print("2. Login as student")
        print("3. Keluar")

        choice = input("Pilih menu: ")

        if choice == '1':
            login_adm()
        elif choice == '2':
            login_mhs()
        elif choice == '3':
            print("Terima kasih, sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang benar.")

if __name__ == "__main__":
    main()

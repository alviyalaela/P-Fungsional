

expenses = [
{'tanggal': '2023-07-25', 'deskripsi': 'Makan Siang', 'jumlah': 50000},
{'tanggal': '2023-07-25', 'deskripsi': 'Transportasi', 'jumlah': 25000},
{'tanggal': '2023-07-26', 'deskripsi': 'Belanja', 'jumlah': 100000},
]

def add_expense(expense):
    innerData = {}
    date = input("Masukkan tanggal pengeluaran (YYYY-MM-DD): ")
    description = input("Masukkan deskripsi pengeluaran: ")
    amount = int(input("Masukkan jumlah pengeluaran: "))
    innerData['tanggal'] = date 
    innerData['deskripsi'] = description
    innerData['jumlah'] = amount
    new_expense = expense[:]
    new_expense.append(innerData)
    return new_expense

def view_expenses_by_date(new_expense):
    date = input("Masukkan tanggal : ")
    filterx = list(filter(lambda x: date == x['tanggal'], new_expense))
    total = 0
    if filterx: 
        total = sum(map(lambda data: data['jumlah'], filterx))
        print(f"tanggal : {date}, total : {total}")
      
        
def view_expenses_report(new_expenses):
    date = input("Masukkan tanggal : ")
    result = [x for x in new_expenses if date == x['tanggal']]
    print(result)


def generate_expense_report(new_expenses):
    for x in new_expenses:
        yield x

def view_generator(data):
    for item in data:
        print(f"Deskripsi : {item['deskripsi']}, Tanggal {item['tanggal']}, Jumlah : {item['jumlah']} ")

def display_menu():
    print("\n===== Aplikasi Pencatat Pengeluaran Harian =====")
    print("1. Tambah Pengeluaran")
    print("2. Total Pengeluaran Harian")
    print("3. Lihat Pengeluaran berdasarkan Tanggal")
    print("4. Lihat Laporan Pengeluaran Harian")
    print("5. Keluar")

def get_user_input(command):
    return int(input(command))

def main():
    while True:
        display_menu()
        choice = get_user_input("Masukkan pilihan: ")
        if choice == 1:
            add_expense(expenses)
        elif choice == 2:
            view_expenses_by_date(expenses)
        elif choice == 3:
            view_expenses_report(expenses)
        elif choice == 4:
            generator = generate_expense_report(expenses)
            view_generator(generator)
        elif choice == 5:
            print("Terima kasih telah menggunakan aplikasi kami.")


if __name__ == "__main__":
    main()
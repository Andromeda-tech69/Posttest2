import os
os.system('cls')

# Inisialisasi data
barang = []


# Role Pembeli
def pembeli_menu():
    print("Menu Pembeli")
    print("1. Transaksi")
    print("2. Keluar")

    pilihan = input("Masukkan pilihan Anda: ")

    if pilihan == "1":
        transaksi()
    elif pilihan == "2":
        print("Terima kasih, sampai jumpa!")
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

# Fitur untuk role pembeli
from prettytable import PrettyTable
from operator import itemgetter

data_barang = [
    ['Paracetamol', 'Rp 6.000'],
    ['Ibuprofen', 'Rp 2.600'],
    ['Tera-F', 'Rp 5.000'],
    ['Diatabs', 'Rp 3.500'],
    ['Benacol DTM Sirup', 'Rp 17.500'],
    ['Entrostop tab', 'Rp 10.000'],
    ['Oralit', 'Rp 1.500'],
    ['Vicks formula anak Sirup', 'Rp 11.000'],
    ['Sanmol', 'Rp 2.000'],
    ['Sanmag sirup', 'Rp 32.500'],
    ['Amoxicillin', 'Rp 8.000'],
    ['Antasida doen', 'Rp 2.500'],
    ['Bodrex', 'Rp 8.000'],
    ['OBH Combi sirup', 'Rp 24.500'],
    ['Ultraflu', 'Rp 3.000']
]

def lihat_barang():
    # Mengurutkan data_barang berdasarkan nama barang
    data_barang_sorted = sorted(data_barang, key=itemgetter(0))
    
    table = PrettyTable (["No.", "Nama Barang", "Harga"])
    for i, barang in enumerate(data_barang_sorted, start=1):
        table.add_row([i, barang[0], barang[1]])
    
    print(table)

def transaksi():
    daftar_pembelian = []
    total_harga = 0

    while True:
        lihat_barang()
        no_barang = input("Masukkan nomor barang yang ingin dibeli (0 untuk selesai): ")
        if no_barang == "0":
            break 

        no_barang = int(no_barang)
        if no_barang < 1 or no_barang > len(data_barang):
            print("Nomor barang tidak valid.")
            continue

        jumlah = int(input("Masukkan jumlah barang yang ingin dibeli: "))
        if jumlah <= 0:
            print("Jumlah barang harus lebih dari 0.")
            continue

        nama_barang = data_barang[no_barang - 1][0]
        harga_barang = float(data_barang[no_barang - 1][1].replace("Rp ", "").replace(",", ""))
        harga_total = harga_barang * jumlah

        daftar_pembelian.append([nama_barang, jumlah, harga_total])
        total_harga += harga_total

        print(f"\nBarang '{nama_barang}' ({jumlah} buah) berhasil ditambahkan ke keranjang.")

    print("\nDaftar Pembelian:")
    table = PrettyTable(["No.", "Nama Barang", "Jumlah", "Harga Total"])
    for i, pembelian in enumerate(daftar_pembelian, start=1):
        table.add_row([i, pembelian[0], pembelian[1], f"Rp {pembelian[2]}"])
    print(table)

    print("\nTotal Harga: Rp", total_harga)
    
    pembeli_menu()
    return

# Memanggil fungsi transaksi()
    transaksi()

# Role Admin
def admin_menu():
    print("Menu Admin")
    print("1. Lihat Barang")
    print("2. Tambah Barang")
    print("3. Ubah Barang")
    print("4. Hapus Barang")
    print("5. Keluar")

    pilihan = input("Masukkan pilihan Anda: ")

    if pilihan == "1":
        lihat_barang()
    elif pilihan == "2":
        tambah_barang()
    elif pilihan == "3":
        ubah_barang()
    elif pilihan == "4":
        hapus_barang()
    elif pilihan == "5":
        print("Terima kasih, sampai jumpa!")
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

# Fitur untuk role admin
from prettytable import PrettyTable
from operator import itemgetter

data_barang = [
    ['Paracetamol', 'Rp 6.000'],
    ['Ibuprofen', 'Rp 2.600'],
    ['Tera-F', 'Rp 5.000'],
    ['Diatabs', 'Rp 3.500'],
    ['Benacol DTM Sirup', 'Rp 17.500'],
    ['Entrostop tab', 'Rp 10.000'],
    ['Oralit', 'Rp 1.500'],
    ['Vicks formula anak Sirup', 'Rp 11.000'],
    ['Sanmol', 'Rp 2.000'],
    ['Sanmag sirup', 'Rp 32.500'],
    ['Amoxicillin', 'Rp 8.000'],
    ['Antasida doen', 'Rp 2.500'],
    ['Bodrex', 'Rp 8.000'],
    ['OBH Combi sirup', 'Rp 24.500'],
    ['Ultraflu', 'Rp 3.000']
]

def lihat_barang():
    # Mengurutkan data_barang berdasarkan nama barang
    data_barang_sorted = sorted(data_barang, key=itemgetter(0))
    
    table = PrettyTable(["No.", "Nama Barang", "Harga"])
    for i, barang in enumerate(data_barang_sorted, start=1):
        table.add_row([i, barang[0], barang[1]])
    
    print(table)

def tambah_barang():
    no = len(data_barang) + 1
    nama_barang = input("Nama Barang: ")
    harga = input("Harga: ")
    data_barang.append([nama_barang, harga])
    print("Barang berhasil ditambahkan.")

def ubah_barang():
    no_barang = int(input("Masukkan nomor barang yang ingin diubah: "))
    if no_barang < 1 or no_barang > len(data_barang):
        print("Nomor barang tidak valid.")
        return
    
    nama_barang = input("Nama Barang baru: ")
    harga = input("Harga baru: ")
    data_barang[no_barang - 1] = [nama_barang, harga]
    print("Barang berhasil diubah.")

def hapus_barang():
    no_barang = int(input("Masukkan nomor barang yang ingin dihapus: "))
    if no_barang < 1 or no_barang > len(data_barang):
        print("Nomor barang tidak valid.")
        return
    
    data_barang.pop(no_barang - 1)
    print("Barang berhasil dihapus.")

# Memanggil fungsi lihat_barang() untuk menampilkan daftar barang awal
lihat_barang()

# Main Program
def main():
    while True:
        print("Selamat datang di Program Barang")
        print("1. Pembeli")
        print("2. Admin")
        print("3. Keluar")

        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == "1":
            pembeli_menu()
        elif pilihan == "2":
            admin_menu()
        elif pilihan == "3":
            print ("Terima kasih")
            print ("Sampai Jumpa")
            print ("=============")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Jalankan program utama
main()

# Posttest2
# Andromeda Hibnu Darmawi
# NIM 2309116038
# Kelas Sistem Informasi A
# Menu Program
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

# Jalankan program
main()

# Output
# 1. Pembeli
Masukkan pilihan Anda: 1
Menu Pembeli
1. Transaksi
2. Keluar
# 2. Admin
Masukkan pilihan Anda: 2
Menu Admin
1. Lihat Barang
2. Tambah Barang
3. Ubah Barang
4. Hapus Barang
5. Keluar
# 3. Keluar
Masukkan pilihan Anda: 3
Terima kasih
Sampai Jumpa
=============


# menu pembeli
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

# Output
# 1. Transaksi
Masukkan pilihan Anda: 1
Menu Pembeli
1. Transaksi
2. Keluar
Masukkan pilihan Anda: 1
+-----+--------------------------+-----------+
| No. |       Nama Barang        |   Harga   |
+-----+--------------------------+-----------+
|  1  |       Amoxicillin        |  Rp 8.000 |
|  2  |      Antasida doen       |  Rp 2.500 |
|  3  |    Benacol DTM Sirup     | Rp 17.500 |
|  4  |          Bodrex          |  Rp 8.000 |
|  5  |         Diatabs          |  Rp 3.500 |
|  6  |      Entrostop tab       | Rp 10.000 |
|  7  |        Ibuprofen         |  Rp 2.600 |
|  8  |     OBH Combi sirup      | Rp 24.500 |
|  9  |          Oralit          |  Rp 1.500 |
|  10 |       Paracetamol        |  Rp 6.000 |
|  11 |       Sanmag sirup       | Rp 32.500 |
|  12 |          Sanmol          |  Rp 2.000 |
|  13 |          Tera-F          |  Rp 5.000 |
|  14 |         Ultraflu         |  Rp 3.000 |
|  15 | Vicks formula anak Sirup | Rp 11.000 |
+-----+--------------------------+-----------+
Masukkan nomor barang yang ingin dibeli (0 untuk selesai): 5
Masukkan jumlah barang yang ingin dibeli: 2

Barang 'Benacol DTM Sirup' (2 buah) berhasil ditambahkan ke keranjang.
+-----+--------------------------+-----------+
| No. |       Nama Barang        |   Harga   |
+-----+--------------------------+-----------+
|  1  |       Amoxicillin        |  Rp 8.000 |
|  2  |      Antasida doen       |  Rp 2.500 |
|  3  |    Benacol DTM Sirup     | Rp 17.500 |
|  4  |          Bodrex          |  Rp 8.000 |
|  5  |         Diatabs          |  Rp 3.500 |
|  6  |      Entrostop tab       | Rp 10.000 |
|  7  |        Ibuprofen         |  Rp 2.600 |
|  8  |     OBH Combi sirup      | Rp 24.500 |
|  9  |          Oralit          |  Rp 1.500 |
|  10 |       Paracetamol        |  Rp 6.000 |
|  11 |       Sanmag sirup       | Rp 32.500 |
|  12 |          Sanmol          |  Rp 2.000 |
|  13 |          Tera-F          |  Rp 5.000 |
|  14 |         Ultraflu         |  Rp 3.000 |
|  15 | Vicks formula anak Sirup | Rp 11.000 |
+-----+--------------------------+-----------+
Masukkan nomor barang yang ingin dibeli (0 untuk selesai): 11
Masukkan jumlah barang yang ingin dibeli: 1

Barang 'Amoxicillin' (1 buah) berhasil ditambahkan ke keranjang.
+-----+--------------------------+-----------+
| No. |       Nama Barang        |   Harga   |
+-----+--------------------------+-----------+
|  1  |       Amoxicillin        |  Rp 8.000 |
|  2  |      Antasida doen       |  Rp 2.500 |
|  3  |    Benacol DTM Sirup     | Rp 17.500 |
|  4  |          Bodrex          |  Rp 8.000 |
|  5  |         Diatabs          |  Rp 3.500 |
|  6  |      Entrostop tab       | Rp 10.000 |
|  7  |        Ibuprofen         |  Rp 2.600 |
|  8  |     OBH Combi sirup      | Rp 24.500 |
|  9  |          Oralit          |  Rp 1.500 |
|  10 |       Paracetamol        |  Rp 6.000 |
|  11 |       Sanmag sirup       | Rp 32.500 |
|  12 |          Sanmol          |  Rp 2.000 |
|  13 |          Tera-F          |  Rp 5.000 |
|  14 |         Ultraflu         |  Rp 3.000 |
|  15 | Vicks formula anak Sirup | Rp 11.000 |
+-----+--------------------------+-----------+
Masukkan nomor barang yang ingin dibeli (0 untuk selesai): 14
Masukkan jumlah barang yang ingin dibeli: 3

Barang 'OBH Combi sirup' (3 buah) berhasil ditambahkan ke keranjang.
+-----+--------------------------+-----------+
| No. |       Nama Barang        |   Harga   |
+-----+--------------------------+-----------+
|  1  |       Amoxicillin        |  Rp 8.000 |
|  2  |      Antasida doen       |  Rp 2.500 |
|  3  |    Benacol DTM Sirup     | Rp 17.500 |
|  4  |          Bodrex          |  Rp 8.000 |
|  5  |         Diatabs          |  Rp 3.500 |
|  6  |      Entrostop tab       | Rp 10.000 |
|  7  |        Ibuprofen         |  Rp 2.600 |
|  8  |     OBH Combi sirup      | Rp 24.500 |
|  9  |          Oralit          |  Rp 1.500 |
|  10 |       Paracetamol        |  Rp 6.000 |
|  11 |       Sanmag sirup       | Rp 32.500 |
|  12 |          Sanmol          |  Rp 2.000 |
|  13 |          Tera-F          |  Rp 5.000 |
|  14 |         Ultraflu         |  Rp 3.000 |
|  15 | Vicks formula anak Sirup | Rp 11.000 |
+-----+--------------------------+-----------+
Masukkan nomor barang yang ingin dibeli (0 untuk selesai): 0

Daftar Pembelian:
+-----+-------------------+--------+-------------+
| No. |    Nama Barang    | Jumlah | Harga Total |
+-----+-------------------+--------+-------------+
|  1  | Benacol DTM Sirup |   2    |   Rp 35.0   |
|  2  |    Amoxicillin    |   1    |    Rp 8.0   |
|  3  |  OBH Combi sirup  |   3    |   Rp 73.5   |
+-----+-------------------+--------+-------------+

Total Harga: Rp 116.5
Menu Pembeli
1. Transaksi
2. Keluar

# 2. Keluar
Masukkan pilihan Anda: 2
Terima kasih, sampai jumpa!
Selamat datang di Program Barang
1. Pembeli
2. Admin
3. Keluar

# 2. Menu admin
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

#Output
# 1. Lihat barang
Selamat datang di Program Barang
1. Pembeli
2. Admin
3. Keluar
Masukkan pilihan Anda: 2
Menu Admin
1. Lihat Barang
2. Tambah Barang
3. Ubah Barang
4. Hapus Barang
5. Keluar
Masukkan pilihan Anda: 1
+-----+--------------------------+-----------+
| No. |       Nama Barang        |   Harga   |
+-----+--------------------------+-----------+
|  1  |       Amoxicillin        |  Rp 8.000 |
|  2  |      Antasida doen       |  Rp 2.500 |
|  3  |    Benacol DTM Sirup     | Rp 17.500 |
|  4  |          Bodrex          |  Rp 8.000 |
|  5  |         Diatabs          |  Rp 3.500 |
|  6  |      Entrostop tab       | Rp 10.000 |
|  7  |        Ibuprofen         |  Rp 2.600 |
|  8  |     OBH Combi sirup      | Rp 24.500 |
|  9  |          Oralit          |  Rp 1.500 |
|  10 |       Paracetamol        |  Rp 6.000 |
|  11 |       Sanmag sirup       | Rp 32.500 |
|  12 |          Sanmol          |  Rp 2.000 |
|  13 |          Tera-F          |  Rp 5.000 |
|  14 |         Ultraflu         |  Rp 3.000 |
|  15 | Vicks formula anak Sirup | Rp 11.000 |
+-----+--------------------------+-----------+
Selamat datang di Program Barang
1. Pembeli
2. Admin
3. Keluar

# 2. Tambah barang
Selamat datang di Program Barang
1. Pembeli
2. Admin
3. Keluar
Masukkan pilihan Anda: 2
Menu Admin
1. Lihat Barang
2. Tambah Barang
3. Ubah Barang
4. Hapus Barang
5. Keluar
Masukkan pilihan Anda: 2
Nama Barang: Dentasol
Harga: Rp. 15.000 
Barang berhasil ditambahkan.
+-----+--------------------------+------------+
| No. |       Nama Barang        |   Harga    |
+-----+--------------------------+------------+
|  1  |       Amoxicillin        |  Rp 8.000  |
|  2  |      Antasida doen       |  Rp 2.500  |
|  3  |    Benacol DTM Sirup     | Rp 17.500  |
|  4  |          Bodrex          |  Rp 8.000  |
|  5  |         Dentasol         | Rp. 15.000 |
|  6  |         Diatabs          |  Rp 3.500  |
|  7  |      Entrostop tab       | Rp 10.000  |
|  8  |        Ibuprofen         |  Rp 2.600  |
|  9  |     OBH Combi sirup      | Rp 24.500  |
|  10 |          Oralit          |  Rp 1.500  |
|  11 |       Paracetamol        |  Rp 6.000  |
|  12 |       Sanmag sirup       | Rp 32.500  |
|  13 |          Sanmol          |  Rp 2.000  |
|  14 |          Tera-F          |  Rp 5.000  |
|  15 |         Ultraflu         |  Rp 3.000  |
|  16 | Vicks formula anak Sirup | Rp 11.000  |
+-----+--------------------------+------------+

# 3. Ubah barang
Selamat datang di Program Barang
1. Pembeli
2. Admin
3. Keluar
Masukkan pilihan Anda: 2
Menu Admin
1. Lihat Barang
2. Tambah Barang
3. Ubah Barang
4. Hapus Barang
5. Keluar
Masukkan pilihan Anda: 3
Masukkan nomor barang yang ingin diubah: 4
Nama Barang baru: Eugenia Dental
Harga baru: Rp. 25.000
Barang berhasil diubah.
+-----+--------------------------+------------+
|  1  |       Amoxicillin        |  Rp 8.000  |
|  2  |      Antasida doen       |  Rp 2.500  |
|  3  |    Benacol DTM Sirup     | Rp 17.500  |
|  4  |          Bodrex          |  Rp 8.000  |
|  5  |         Dentasol         | Rp. 15.000 |
|  6  |      Entrostop tab       | Rp 10.000  |
|  7  |      Eugenia Dental      | Rp. 25.000 |
|  8  |        Ibuprofen         |  Rp 2.600  |
|  9  |     OBH Combi sirup      | Rp 24.500  |
|  10 |          Oralit          |  Rp 1.500  |
|  11 |       Paracetamol        |  Rp 6.000  |
|  12 |       Sanmag sirup       | Rp 32.500  |
|  13 |          Sanmol          |  Rp 2.000  |
|  14 |          Tera-F          |  Rp 5.000  |
|  15 |         Ultraflu         |  Rp 3.000  |
|  16 | Vicks formula anak Sirup | Rp 11.000  |
+-----+--------------------------+------------+

# 4. Hapus barang
Selamat datang di Program Barang
1. Pembeli
2. Admin
3. Keluar
Masukkan pilihan Anda: 2
Menu Admin
1. Lihat Barang
2. Tambah Barang
3. Ubah Barang
4. Hapus Barang
5. Keluar
Masukkan pilihan Anda: 4
Masukkan nomor barang yang ingin dihapus: 5
Barang berhasil dihapus.
+-----+--------------------------+-----------+
| No. |       Nama Barang        |   Harga   |
+-----+--------------------------+-----------+
|  1  |       Amoxicillin        |  Rp 8.000 |
|  2  |      Antasida doen       |  Rp 2.500 |
|  3  |          Bodrex          |  Rp 8.000 |
|  4  |         Diatabs          |  Rp 3.500 |
|  5  |      Entrostop tab       | Rp 10.000 |
|  6  |        Ibuprofen         |  Rp 2.600 |
|  7  |     OBH Combi sirup      | Rp 24.500 |
|  8  |          Oralit          |  Rp 1.500 |
|  9  |       Paracetamol        |  Rp 6.000 |
|  10 |       Sanmag sirup       | Rp 32.500 |
|  11 |          Sanmol          |  Rp 2.000 |
|  12 |          Tera-F          |  Rp 5.000 |
|  13 |         Ultraflu         |  Rp 3.000 |
|  14 | Vicks formula anak Sirup | Rp 11.000 |
+-----+--------------------------+-----------+

# 5. Keluar
Selamat datang di Program Barang
1. Pembeli
2. Admin
3. Keluar
Masukkan pilihan Anda: 2
Menu Admin
1. Lihat Barang
2. Tambah Barang
3. Ubah Barang
4. Hapus Barang
5. Keluar
Masukkan pilihan Anda: 5
Terima kasih, sampai jumpa!
Selamat datang di Program Barang
1. Pembeli
2. Admin
3. Keluar
Masukkan pilihan Anda:

#Sekian dari saya terima kasih

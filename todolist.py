# Fungsi untuk menampilkan menu
def tampilkan_menu():
    print("\n=== Aplikasi To-Do List ===")
    print("1. Tampilkan Daftar Tugas")
    print("2. Tambah Tugas")
    print("3. Hapus Tugas")
    print("4. Simpan Daftar Tugas ke File")
    print("5. Baca Daftar Tugas dari File")
    print("6. Cari Tugas")
    print("7. Keluar")

# Fungsi untuk menampilkan daftar tugas
def tampilkan_tugas(daftar_tugas):
    if not daftar_tugas:
        print("Daftar tugas kosong.")
    else:
        print("\nDaftar Tugas:")
        for i, tugas in enumerate(daftar_tugas, start=1):
            print(f"{i}. {tugas}")

# Fungsi untuk menambahkan tugas
def tambah_tugas(daftar_tugas):
    tugas = input("Masukkan tugas baru: ")
    daftar_tugas.append(tugas)
    print(f"Tugas '{tugas}' berhasil ditambahkan.")

# Fungsi untuk menghapus tugas
def hapus_tugas(daftar_tugas):
    tampilkan_tugas(daftar_tugas)
    try:
        indeks = int(input("Masukkan nomor tugas yang ingin dihapus: ")) - 1
        if 0 <= indeks < len(daftar_tugas):
            tugas = daftar_tugas.pop(indeks)
            print(f"Tugas '{tugas}' berhasil dihapus.")
        else:
            print("Nomor tugas tidak valid.")
    except ValueError:
        print("Input tidak valid. Harap masukkan nomor.")

# Fungsi untuk menyimpan daftar tugas ke file
def simpan_ke_file(daftar_tugas, nama_file="tasks.txt"):
    with open(nama_file, "w") as file:
        for tugas in daftar_tugas:
            file.write(tugas + "\n")
    print(f"Daftar tugas berhasil disimpan ke {nama_file}.")

# Fungsi untuk membaca daftar tugas dari file
def baca_dari_file(daftar_tugas, nama_file="tasks.txt"):
    try:
        with open(nama_file, "r") as file:
            daftar_tugas.clear()
            for line in file:
                daftar_tugas.append(line.strip())
        print(f"Daftar tugas berhasil dimuat dari {nama_file}.")
    except FileNotFoundError:
        print("File tidak ditemukan. Membuat file baru.")

# Fungsi rekursi untuk mencari tugas
def cari_tugas(daftar_tugas, kata_kunci, indeks=0):
    if indeks >= len(daftar_tugas):
        return None
    if kata_kunci.lower() in daftar_tugas[indeks].lower():
        return daftar_tugas[indeks]
    return cari_tugas(daftar_tugas, kata_kunci, indeks + 1)

# Program utama
def main():
    daftar_tugas = []
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-7): ")
        if pilihan == "1":
            tampilkan_tugas(daftar_tugas)
        elif pilihan == "2":
            tambah_tugas(daftar_tugas)
        elif pilihan == "3":
            hapus_tugas(daftar_tugas)
        elif pilihan == "4":
            simpan_ke_file(daftar_tugas)
        elif pilihan == "5":
            baca_dari_file(daftar_tugas)
        elif pilihan == "6":
            kata_kunci = input("Masukkan kata kunci pencarian: ")
            hasil = cari_tugas(daftar_tugas, kata_kunci)
            if hasil:
                print(f"Tugas ditemukan: {hasil}")
            else:
                print("Tugas tidak ditemukan.")
        elif pilihan == "7":
            print("Terima kasih telah menggunakan aplikasi ini. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
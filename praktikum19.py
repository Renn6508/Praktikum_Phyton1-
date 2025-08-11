username = input("Masukkan nama pengguna(username): ")

if username == "admin":
    print("\nSelamat datang,Admin!")
    print("Anda berhasil login sebagai administrator.")
else:
    print(f"\nMaaf, '{username}'bukan admin.")
    print("Akses ditolak")
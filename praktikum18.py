total_belanja = float(input("Masukkan total belanja: Rp "))

if total_belanja > 100000:
    print("\n Selamat,Anda mendapatkan diskon!")
    
    
    diskon = total_belanja * 0.1
    total_setelah_diskon = total_belanja - diskon
    
    print(f"Total belanja: Rp {total_belanja:,.2f}")
    print(f"Diskon 10%: Rp {diskon:,.2f}")
    print(f"Total setelah diskon: Rp {total_setelah_diskon:,.2f}")
    
else:
    print("\nAnda belum mendapatkan diskon.")
    print("Belanja minimal Rp 100.000 untuk mendapatkan diskon 10%")
    print(f"Total belanja: Rp {total_belanja:,.2f}")

print("\nTerima kasih sudah berbelanja!")
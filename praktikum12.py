harga_a = 125000
harga_b = 7300
harga_c = 2850

jumlah_a = int(input("Masukkan jumlah barang A:") )
jumlah_b = int(input("Masukkan jumlah barang B:") )
jumlah_c = int(input("Masukkan jumlah barang C:") )

total_kotor = (jumlah_a * harga_a) + (jumlah_b * harga_b) + (jumlah_c * harga_c)

if total_kotor > 150000:
    diskon = 0.15
elif total_kotor > 100000:
    diskon = 0.10
else:
    diskon = 0.0

jumlah_diskon = total_kotor * diskon
total_bersih = total_kotor - jumlah_diskon

print(f"\nTotal harga kotor : Rp {int(total_kotor):,}".replace(",", "."))
print(f"Diskon ({int(diskon*100)}%) : Rp {int(jumlah_diskon):,}".replace(",", "."))
print(f"Total harga bersih : Rp {int(total_bersih) :,}".replace(",", "."))
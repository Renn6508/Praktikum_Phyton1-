print("PROGRAM PENENTUAN STATUS KELULUSAN SISWA")
print("="*45)


matematika = float(input("Masukkan nilai Matematika: "))
bahasa_indonesia = float(input("Masukkan nilai Bahasa Indonesia: "))
ipa = float(input("Masukkan nilai IPA: "))

rata_rata = (matematika + bahasa_indonesia + ipa) / 3

print(f"\nNilai Matematika: {matematika}")
print(f"Nilai Bahasa Indonesia: {bahasa_indonesia}")
print(f"Nilai IPA: {ipa}")
print(f"Rata-rata: {rata_rata:.2f}")

nilai_dibawah_70 = 0
if matematika < 70:
    nilai_dibawah_70 += 1
if bahasa_indonesia < 70:
    nilai_dibawah_70 += 1
if ipa < 70:
    nilai_dibawah_70 += 1

nilai_diatas_80 = 0
if matematika > 80:
    nilai_diatas_80 += 1
if bahasa_indonesia > 80:
    nilai_diatas_80 += 1
if ipa > 80:
    nilai_diatas_80 += 1

print(f"\nJumlah nilai < 70: {nilai_dibawah_70}")
print(f"Jumlah nilai > 80: {nilai_diatas_80}")


if matematika >= 85 and bahasa_indonesia >= 85 and ipa >= 85:
    status = "LULUS DENGAN PREDIKAT ISTIMEWA"
    
elif nilai_dibawah_70 >= 2:
    status = "TIDAK LULUS"
    
elif nilai_dibawah_70 == 1 and nilai_diatas_80 >= 2:
    status = "LULUS BERSYARAT"
    
elif matematika >= 70 and bahasa_indonesia >= 70 and ipa >= 70 and rata_rata >= 75:
    status = "LULUS"
    
else:
    status = "TIDAK LULUS"

print(f"\nSTATUS KELULUSAN: {status}")
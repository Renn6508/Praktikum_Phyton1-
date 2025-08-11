nama = "Wilhelmina Lorenzia Wijaya"
umur = 17
berat_badan = 45
tinggi_badan = 170
bmi = berat_badan / ((tinggi_badan / 100) ** 2)
status_siswa = True

print ("Nama:", nama)
print ("Umur:", umur + 1, "tahun")
print ("berat_badan:", berat_badan, "kg")
print ("BMI:", round(bmi, 2))
print("Siswa Aktif:", bool(status_siswa))
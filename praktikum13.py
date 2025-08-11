# Program Status Kelulusan Siswa
# Praktikum 13 Python: Operator Perbandingan

print("=" * 50)
print("PROGRAM PENENTUAN STATUS KELULUSAN SISWA")
print("=" * 50)
print("Mata Pelajaran: Matematika, Bahasa Indonesia, IPA")
print("Rentang Nilai: 0 - 100")
print()

# Input nilai dari user
try:
    matematika = float(input("Masukkan nilai Matematika (0-100): "))
    bahasa_indonesia = float(input("Masukkan nilai Bahasa Indonesia (0-100): "))
    ipa = float(input("Masukkan nilai IPA (0-100): "))
    
    # Validasi input nilai dalam rentang 0-100
    if not (0 <= matematika <= 100) or not (0 <= bahasa_indonesia <= 100) or not (0 <= ipa <= 100):
        print("Error: Nilai harus berada dalam rentang 0-100!")
    else:
        print("\n" + "-" * 40)
        print("HASIL EVALUASI:")
        print("-" * 40)
        print(f"Nilai Matematika: {matematika}")
        print(f"Nilai Bahasa Indonesia: {bahasa_indonesia}")
        print(f"Nilai IPA: {ipa}")
        
        # Hitung rata-rata
        rata_rata = (matematika + bahasa_indonesia + ipa) / 3
        print(f"Nilai Rata-rata: {rata_rata:.2f}")
        
        # Hitung jumlah mata pelajaran dengan nilai < 70
        nilai_dibawah_70 = sum([matematika < 70, bahasa_indonesia < 70, ipa < 70])
        
        # Hitung jumlah mata pelajaran dengan nilai > 80
        nilai_diatas_80 = sum([matematika > 80, bahasa_indonesia > 80, ipa > 80])
        
        print("\n" + "=" * 40)
        print("STATUS KELULUSAN:")
        print("=" * 40)
        
        # Logika penentuan status kelulusan
        if matematika >= 85 and bahasa_indonesia >= 85 and ipa >= 85:
            # Ketentuan 5: Semua nilai di atas 85
            status = "LULUS DENGAN PREDIKAT ISTIMEWA"
            print(f"✅ {status}")
            print("🌟 Selamat! Semua nilai Anda sangat memuaskan (≥85)")
            
        elif nilai_dibawah_70 >= 2:
            # Ketentuan 4: Dua atau lebih mata pelajaran di bawah 70
            status = "TIDAK LULUS"
            print(f"❌ {status}")
            print(f"📝 {nilai_dibawah_70} mata pelajaran memiliki nilai di bawah 70")
            
        elif nilai_dibawah_70 == 1 and nilai_diatas_80 >= 2:
            # Ketentuan 3: Satu mata pelajaran di bawah 70, tetapi dua lainnya di atas 80
            status = "LULUS BERSYARAT"
            print(f"⚠️ {status}")
            print("📝 1 mata pelajaran di bawah 70, tapi 2 lainnya di atas 80")
            
        elif matematika >= 70 and bahasa_indonesia >= 70 and ipa >= 70 and rata_rata >= 75:
            # Ketentuan 1 & 2: Semua nilai ≥ 70 dan rata-rata ≥ 75
            status = "LULUS"
            print(f"✅ {status}")
            print("📝 Memenuhi nilai minimal dan rata-rata yang dipersyaratkan")
            
        else:
            # Tidak memenuhi syarat lulus
            status = "TIDAK LULUS"
            print(f"❌ {status}")
            if rata_rata < 75:
                print("📝 Rata-rata kurang dari 75")
            if nilai_dibawah_70 > 0:
                print(f"📝 {nilai_dibawah_70} mata pelajaran memiliki nilai di bawah 70")
        
        print("\n" + "-" * 40)
        print("DETAIL ANALISIS:")
        print("-" * 40)
        print(f"• Mata pelajaran dengan nilai < 70: {nilai_dibawah_70}")
        print(f"• Mata pelajaran dengan nilai > 80: {nilai_diatas_80}")
        print(f"• Rata-rata memenuhi syarat (≥75): {'Ya' if rata_rata >= 75 else 'Tidak'}")
        
        # Saran perbaikan jika tidak lulus
        if status in ["TIDAK LULUS", "LULUS BERSYARAT"]:
            print("\n" + "💡 SARAN PERBAIKAN:")
            if matematika < 70:
                print(f"  - Tingkatkan nilai Matematika (saat ini: {matematika})")
            if bahasa_indonesia < 70:
                print(f"  - Tingkatkan nilai Bahasa Indonesia (saat ini: {bahasa_indonesia})")
            if ipa < 70:
                print(f"  - Tingkatkan nilai IPA (saat ini: {ipa})")
            if rata_rata < 75:
                print(f"  - Tingkatkan rata-rata ke minimal 75 (saat ini: {rata_rata:.2f})")
        
except ValueError:
    print("Error: Masukkan nilai berupa angka yang valid!")
except Exception as e:
    print(f"Error: {e}")

print("\n" + "=" * 50)
print("Terima kasih telah menggunakan program ini!")
print("=" * 50)
print("PROGRAM KALKULATOR SKOR GAMER")

skor = 0
print(f"Skor awal: {skor}")

skor += 120
print(f"Setelah Misi 1 (+120): {skor}")

skor += 150
print(f"Setelah Misi 2 (+150): {skor}")

skor += 100
print(f"Setelah Misi 3 (+100): {skor}")

skor -= 50
print(f"Setelah penalti (-50): {skor}")

skor *= 2
print(f"Setelah bonus 2x: {skor}")

skor -= 30
print(f"Setelah kesalahan teknis (-30): {skor}")

print("="*35)
print(f"SKOR AKHIR: {skor}")
print("="*35)
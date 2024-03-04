# Fungsi untuk menghitung nilai keanggotaan
def fuzzy_membership(x, a, b, c):
    if x <= a or x >= c:
        return 0
    elif a < x < b:
        return (x - a) / (b - a)
    elif b <= x <= c:
        return (c - x) / (c - b)

# Fungsi main
def main(permintaan, persediaan):
    # Batasan produksi
    batasan_produksi = 5000
    min_produksi = 1500
    
    # Perhitungan keanggotaan
    R1 = min(fuzzy_membership(permintaan, 1000, 2000, 4000), fuzzy_membership(persediaan, 100, 300, 500))
    R2 = min(fuzzy_membership(permintaan, 1000, 2000, 4000), fuzzy_membership(persediaan, 300, 400, 500))
    R3 = min(fuzzy_membership(permintaan, 2000, 3000, 4000), fuzzy_membership(persediaan, 100, 300, 500))
    RA = min(fuzzy_membership(permintaan, 2000, 3000, 4000), fuzzy_membership(persediaan, 300, 400, 500))

    # Menggunakan aturan fuzzy Tsukamoto
    produksi = max(min_produksi, (R1*1000 + R2*1000 + R3*4000 + RA*4000) / (R1 + R2 + R3 + RA))
    
    # Jika produksi melebihi batasan produksi, produksi diatur menjadi batasan produksi
    produksi = min(produksi, batasan_produksi)
    
    return produksi

# Input permintaan dan persediaan
permintaan = 3000
persediaan = 300

# Hitung jumlah unit yang harus diproduksi
jumlah_produksi = main(permintaan, persediaan)
print("Jumlah unit mobil mobilan jenis XYZ yang harus diproduksi:", jumlah_produksi, "unit")

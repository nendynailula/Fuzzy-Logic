# Import library
import numpy as np

# Fungsi keanggotaan untuk permintaan
def permintaan_turun(permintaan):
    if permintaan <= 1000:
        return 1
    elif permintaan > 1000 and permintaan < 3000:
        return (3000 - permintaan) / 2000
    else:
        return 0

def permintaan_nok(permintaan):
    if permintaan <= 1000 or permintaan >= 4000:
        return 0
    elif permintaan > 1000 and permintaan < 3000:
        return (permintaan - 1000) / 2000
    elif permintaan >= 3000 and permintaan < 4000:
        return (4000 - permintaan) / 1000

# Fungsi keanggotaan untuk persediaan
def persediaan_banyak(persediaan):
    if persediaan <= 100:
        return 1
    elif persediaan > 100 and persediaan < 300:
        return (300 - persediaan) / 200
    else:
        return 0

def persediaan_sedikit(persediaan):
    if persediaan <= 100:
        return 0
    elif persediaan > 100 and persediaan < 300:
        return (persediaan - 100) / 200
    else:
        return 1

# Fungsi keanggotaan untuk produksi
def produksi_kurang(produksi):
    return produksi / 5000

def produksi_tambah(produksi):
    return produksi / 5000

# Aturan fuzzy
def fuzzy_rule(permintaan, persediaan):
    rule1 = min(permintaan_turun(permintaan), persediaan_banyak(persediaan))
    rule2 = min(permintaan_turun(permintaan), persediaan_sedikit(persediaan))
    rule3 = min(permintaan_nok(permintaan), persediaan_banyak(persediaan))
    rule4 = min(permintaan_nok(permintaan), persediaan_sedikit(persediaan))
    return [rule1, rule2, rule3, rule4]

# Fuzzy inference
def fuzzy_inference(permintaan, persediaan):
    rules = fuzzy_rule(permintaan, persediaan)
    produksi = (rules[0]*produksi_kurang(permintaan) + 
                rules[1]*produksi_kurang(permintaan) + 
                rules[2]*produksi_tambah(permintaan) + 
                rules[3]*produksi_tambah(permintaan))
    return produksi

# Defuzzifikasi
def defuzzifikasi(permintaan, persediaan):
    produksi = fuzzy_inference(permintaan, persediaan)
    return produksi * 5000

# Input permintaan dan persediaan
permintaan = 3000
persediaan = 300

# Output produksi
print("Jumlah unit mobil mobilan jenis XYZ yang harus diproduksi:", defuzzifikasi(permintaan, persediaan))

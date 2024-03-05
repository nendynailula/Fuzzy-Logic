import numpy as np

# Fungsi keanggotaan untuk permintaan
def permintaan_turun(x):
    if x <= 2000:
        return 1
    elif x > 5000 and x < 6000:
        return (5000 - x) / (6000 - 5000)
    else:
        return 0

def permintaan_naik(x):
    if x >= 5000:
        return 1
    elif x > 2000 and x < 5000:
        return (x - 2000) / (2000 - 5000)
    else:
        return 0

# Fungsi keanggotaan untuk persediaan
def persediaan_banyak(x):
    if x <= 200:
        return 1
    elif x > 200 and x < 700:
        return (700 - x) / (700 - 500)
    else:
        return 0

def persediaan_sedikit(x):
    if x >= 700:
        return 1
    elif x > 200 and x < 700:
        return (x - 200) / (700 - 200)
    else:
        return 0

# Inferensi Mamdani
def mamdani_inference(permintaan, persediaan):
    # Evaluasi aturan fuzzy
    produksi_berkurang = min(permintaan_turun(permintaan), persediaan_banyak(persediaan))
    produksi_tidak_berkurang = min(permintaan_turun(permintaan), persediaan_sedikit(persediaan))
    produksi_tidak_berkurang += min(permintaan_naik(permintaan), persediaan_banyak(persediaan))
    produksi_berkurang += min(permintaan_naik(permintaan), persediaan_sedikit(persediaan))

    # Gabungkan aturan fuzzy dengan operator OR
    produksi = max(produksi_berkurang, produksi_tidak_berkurang)

    return produksi

# Permintaan bulan ini dan persediaan di gudang
permintaan_bulan_ini = 5000
persediaan_di_gudang = 400

# Menggunakan metode Mamdani untuk menentukan jumlah produksi
jumlah_produksi = mamdani_inference(permintaan_bulan_ini, persediaan_di_gudang) * 8000  # Maksimum produksi
print("Jumlah Produksi yang Direkomendasikan:", jumlah_produksi, "unit")

import numpy as np

# Fungsi keanggotaan untuk permintaan
def permintaan_turun(x):
    if x <= 2000:
        return 1
    elif x > 2000 and x < 5000:
        return (5000 - x) / (5000 - 2000)
    else:
        return 0

def permintaan_naik(x):
    if x >= 5000:
        return 1
    elif x > 2000 and x < 5000:
        return (x - 2000) / (5000 - 2000)
    else:
        return 0

# Fungsi keanggotaan untuk persediaan
def persediaan_banyak(x):
    if x <= 200:
        return 1
    elif x > 200 and x < 700:
        return (700 - x) / (700 - 200)
    else:
        return 0

def persediaan_sedikit(x):
    if x >= 700:
        return 1
    elif x > 200 and x < 700:
        return (x - 200) / (700 - 200)
    else:
        return 0

# Inferensi Sugeno
def sugeno_inference(permintaan, persediaan):
    produksi_berkurang = min(permintaan_turun(permintaan), persediaan_banyak(persediaan))
    produksi_tidak_berkurang = min(permintaan_turun(permintaan), persediaan_sedikit(persediaan))
    produksi_tidak_berkurang += min(permintaan_naik(permintaan), persediaan_banyak(persediaan))
    produksi_berkurang += min(permintaan_naik(permintaan), persediaan_sedikit(persediaan))
    
    # Menggunakan metode Sugeno untuk defuzzifikasi
    produksi = (0*produksi_berkurang + 2000*produksi_tidak_berkurang) / (produksi_berkurang + produksi_tidak_berkurang)
    
    return produksi

# Permintaan bulan ini dan persediaan di gudang
permintaan_bulan_ini = 5000
persediaan_di_gudang = 400

# Menggunakan metode Sugeno untuk menentukan jumlah produksi
jumlah_produksi = sugeno_inference(permintaan_bulan_ini, persediaan_di_gudang)
print("Jumlah Produksi yang Direkomendasikan:", jumlah_produksi, "unit")

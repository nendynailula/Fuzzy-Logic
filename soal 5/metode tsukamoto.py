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

# Metode Fuzzy Tsukamoto
def tsukamoto_inference(permintaan, persediaan):
    # Nilai produksi jika permintaan turun
    produksi_turun = min(permintaan_turun(permintaan), persediaan_banyak(persediaan)) * 2000
    
    # Nilai produksi jika permintaan naik
    produksi_naik = min(permintaan_naik(permintaan), persediaan_sedikit(persediaan)) * 6000
    
    # Menggabungkan kedua nilai produksi menggunakan metode Tsukamoto
    produksi = max(produksi_turun, produksi_naik)
    
    return produksi

# Permintaan bulan ini dan persediaan di gudang
permintaan_bulan_ini = 5000
persediaan_di_gudang = 400

# Menggunakan metode Tsukamoto untuk menentukan jumlah produksi
jumlah_produksi = tsukamoto_inference(permintaan_bulan_ini, persediaan_di_gudang)
print("Jumlah Produksi yang Direkomendasikan:", jumlah_produksi, "unit")

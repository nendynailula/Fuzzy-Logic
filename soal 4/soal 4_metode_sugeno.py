# Fungsi keanggotaan untuk variabel permintaan
def turun(permintaan):
    if permintaan <= 5000:
        return 1
    elif permintaan > 5000 and permintaan < 8000:
        return (8000 - permintaan) / (8000 - 5000)
    else:
        return 0

def naik(permintaan):
    if permintaan <= 5000:
        return 0
    elif permintaan > 5000 and permintaan < 8000:
        return (permintaan - 5000) / (8000 - 5000)
    else:
        return 1

# Fungsi keanggotaan untuk variabel persediaan
def sedikit(persediaan):
    if persediaan <= 500:
        return 1
    elif persediaan > 500 and persediaan < 1000:
        return (1000 - persediaan) / (1000 - 500)
    else:
        return 0

def banyak(persediaan):
    if persediaan <= 500:
        return 0
    elif persediaan > 500 and persediaan < 1000:
        return (persediaan - 500) / (1000 - 500)
    else:
        return 1

# Inferensi menggunakan aturan fuzzy
def inferensi(permintaan, persediaan):
    produksi = {}
    
    # R1: Jika permintaan turun dan persediaan banyak, maka produksi berkurang
    produksi['R1'] = min(turun(permintaan), banyak(persediaan))
    
    # R2: Jika permintaan turun dan persediaan sedikit, maka produksi berkurang
    produksi['R2'] = min(turun(permintaan), sedikit(persediaan))
    
    # R3: Jika permintaan naik dan persediaan banyak, maka produksi bertambah
    produksi['R3'] = min(naik(permintaan), banyak(persediaan))
    
    # R4: Jika permintaan naik dan persediaan sedikit, maka produksi bertambah
    produksi['R4'] = min(naik(permintaan), sedikit(persediaan))
    
    return produksi

# Defuzzifikasi menggunakan metode Sugeno
def sugeno(permintaan, persediaan):
    produksi = inferensi(permintaan, persediaan)
    
    # Menghitung nilai produksi menggunakan metode Sugeno
    produksi_values = []
    
    for rule, value in produksi.items():
        if rule == 'R1' or rule == 'R2':
            produksi_values.append(4000 - 0.5 * permintaan - 0.2 * persediaan)  # Menyesuaikan fungsi Sugeno
        elif rule == 'R3' or rule == 'R4':
            produksi_values.append(5000 + 0.7 * permintaan - 0.3 * persediaan)  # Menyesuaikan fungsi Sugeno
    
    # Menghitung rata-rata dari nilai produksi menggunakan metode Sugeno
    return sum(produksi_values) / len(produksi_values)

# Permintaan dan persediaan untuk kasus ini
permintaan = 6000
persediaan = 800

# Menghitung produksi menggunakan metode Sugeno
produksi = sugeno(permintaan, persediaan)
print("Jumlah mobil-mobilan yang harus diproduksi:", produksi)

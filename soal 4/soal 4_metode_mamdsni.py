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

# Defuzzifikasi menggunakan metode Mamdani
def mamdani(permintaan, persediaan):
    produksi = inferensi(permintaan, persediaan)
    
    # Menentukan nilai produksi berdasarkan aturan fuzzy dengan metode Mamdani
    values = []
    
    for rule, value in produksi.items():
        if rule == 'R1' or rule == 'R2':
            values.append(value * 4000)  # Memperbaiki fungsi ini
        elif rule == 'R3' or rule == 'R4':
            values.append(value * 10000)  # Memperbaiki fungsi ini
    
    # Melakukan defuzzifikasi dengan menggunakan metode Mamdani (rata-rata terbobot)
    total_weighted_value = sum(values)
    total_weight = sum(produksi.values())
    
    return total_weighted_value / total_weight

# Permintaan dan persediaan untuk kasus ini
permintaan = 6000
persediaan = 800

# Menghitung produksi menggunakan metode Mamdani
produksi = mamdani(permintaan, persediaan)
print("Jumlah mobil-mobilan yang harus diproduksi:", produksi)

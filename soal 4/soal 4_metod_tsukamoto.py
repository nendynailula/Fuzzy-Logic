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

# Defuzzifikasi menggunakan metode Tsukamoto
def tsukamoto(permintaan, persediaan):
    produksi = inferensi(permintaan, persediaan)
    
    # Menghitung nilai produksi berdasarkan aturan fuzzy dan metode Tsukamoto
    numer = 0
    denom = 0
    
    for rule, value in produksi.items():
        if rule == 'R1':
            numer += value * 4000
            denom += value
        elif rule == 'R2':
            numer += value * 6000
            denom += value
        elif rule == 'R3':
            numer += value * 10000
            denom += value
        elif rule == 'R4':
            numer += value * 10000
            denom += value
    
    return numer / denom

# Permintaan dan persediaan untuk kasus ini
permintaan = 6000
persediaan = 800

# Menghitung produksi menggunakan metode Tsukamoto
produksi = tsukamoto(permintaan, persediaan)
print("Jumlah mobil-mobilan yang harus diproduksi:", produksi)

# Fungsi untuk menentukan produksi berdasarkan aturan fuzzy Tsukamoto
def fuzzy_tsukamoto(permintaan, persediaan):
    # Variabel linguistik
    def kecil(x):
        if x <= 3000:
            return 1
        elif x > 3000 and x < 6000:
            return (6000 - x) / 3000
        else:
            return 0
    
    def besar(x):
        if x >= 6000:
            return 1
        elif x > 3000 and x < 6000:
            return (x - 3000) / 3000
        else:
            return 0
    
    # Inferensi dan Agregasi
    produksi_kecil = min(kecil(permintaan), kecil(persediaan))
    produksi_besar = min(besar(permintaan), besar(persediaan))
    
    # Defuzzyfikasi
    production = (produksi_kecil * 3000 + produksi_besar * 8000) / (produksi_kecil + produksi_besar)
    
    return production

# Fungsi untuk menghitung output Fuzzy Tsukamoto
def calculate_output_tsukamoto(permintaan, persediaan):
    # Hitung produksi menggunakan metode Fuzzy Tsukamoto
    production = fuzzy_tsukamoto(permintaan, persediaan)
    return production

# Fungsi utama untuk metode Fuzzy Tsukamoto
def main_tsukamoto():
    # Input data
    permintaan = 4000 # Permintaan bulan ini
    persediaan = 600 # Persediaan di gudang

    # Hitung output Fuzzy Tsukamoto
    output = calculate_output_tsukamoto(permintaan, persediaan)
    
    # Output hasil produksi
    print("\nMetode Fuzzy Tsukamoto:")
    print("Jumlah mobil mobilan jenis XYZ yang harus diproduksi:", output, "unit")

# Panggil fungsi utama Fuzzy Tsukamoto
main_tsukamoto()

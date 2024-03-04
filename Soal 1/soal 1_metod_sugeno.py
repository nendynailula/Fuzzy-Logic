# Import library yang diperlukan
import numpy as np

# Fungsi untuk menentukan produksi berdasarkan aturan fuzzy
def fuzzy_sugeno(permintaan, persediaan):
    # Inisialisasi variabel
    production = 0
    
    # Aturan Fuzzy
    # R1: Jika permintaan turun dan persediaan banyak, maka produksi berkurang
    if permintaan == "turun" and persediaan == "banyak":
        production = 2000
    # R2: Jika permintaan turun dan persediaan sedikit maka produksi berkurang
    elif permintaan == "turun" and persediaan == "sedikit":
        production = 4000
    # R3: Jika permintaan naik dan persediaan banyak, maka produksi bertambah
    elif permintaan == "naik" and persediaan == "banyak":
        production = 6000
    # RA: Jika permintaan turun dan persediaan sedikit maka produksi bertambah
    elif permintaan == "turun" and persediaan == "sedikit":
        production = 8000
    
    return production

# Fungsi untuk menghitung output Fuzzy Sugeno
def calculate_output(permintaan, persediaan):
    # Hitung produksi menggunakan metode Fuzzy Sugeno
    production = fuzzy_sugeno(permintaan, persediaan)
    return production

# Fungsi utama
def main():
    # Input data
    permintaan = "turun" # Permintaan bulan ini
    persediaan = "sedikit" # Persediaan di gudang

    # Hitung output Fuzzy Sugeno
    output = calculate_output(permintaan, persediaan)
    
    # Output hasil produksi
    print("Jumlah mobil mobilan jenis XYZ yang harus diproduksi:", output, "unit")

# Panggil fungsi utama
if __name__ == "__main__":
    main()

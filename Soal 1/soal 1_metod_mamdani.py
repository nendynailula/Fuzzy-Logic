# Import library yang diperlukan
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib as plt

# Fungsi utama untuk Fuzzy Logic Mamdani
def main_mamdani():
    # Input data
    permintaan = 4000
    persediaan = 600

    # Variabel input dan output
    permintaan_var = ctrl.Antecedent(np.arange(3000, 6000, 1), 'permintaan')
    persediaan_var = ctrl.Antecedent(np.arange(400, 9000, 1), 'persediaan')
    produksi = ctrl.Consequent(np.arange(0, 8000, 1), 'produksi')

    # Fungsi keanggotaan untuk variabel input dan output
    permintaan_var['rendah'] = fuzz.trapmf(permintaan_var.universe, [3000, 3000, 3500, 4500])
    permintaan_var['tinggi'] = fuzz.trapmf(permintaan_var.universe, [3500, 4500, 6000, 6000])
    persediaan_var['sedikit'] = fuzz.trapmf(persediaan_var.universe, [400, 400, 600, 1200])
    persediaan_var['banyak'] = fuzz.trapmf(persediaan_var.universe, [600, 1200, 9000, 9000])
    produksi['sedikit'] = fuzz.trapmf(produksi.universe, [0, 0, 2000, 4000])
    produksi['banyak'] = fuzz.trapmf(produksi.universe, [2000, 4000, 8000, 8000])

    # Aturan fuzzy
    rule1 = ctrl.Rule(permintaan_var['rendah'] & persediaan_var['banyak'], produksi['sedikit'])
    rule2 = ctrl.Rule(permintaan_var['rendah'] & persediaan_var['sedikit'], produksi['sedikit'])
    rule3 = ctrl.Rule(permintaan_var['tinggi'] & persediaan_var['banyak'], produksi['banyak'])
    rule4 = ctrl.Rule(permintaan_var['rendah'] & persediaan_var['sedikit'], produksi['banyak'])

    # Sistem kontrol
    produksi_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4])
    produksi_simulasi = ctrl.ControlSystemSimulation(produksi_ctrl)

    # Masukkan nilai permintaan dan persediaan ke dalam simulasi
    produksi_simulasi.input['permintaan'] = permintaan
    produksi_simulasi.input['persediaan'] = persediaan

    # Jalankan simulasi
    produksi_simulasi.compute()

    # Output hasil produksi
    print("Jumlah mobil mobilan jenis XYZ yang harus diproduksi (Fuzzy Mamdani):", produksi_simulasi.output['produksi'], "unit")

    permintaan_var.view()
    persediaan_var.view()
    produksi.view()
    plt.show()
    plt.waitk
# Panggil fungsi utama untuk Fuzzy Logic Mamdani
if __name__ == "__main__":
    main_mamdani()

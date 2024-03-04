# Impor library yang diperlukan
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Variabel input
permintaan = ctrl.Antecedent(np.arange(0, 5001, 1), 'permintaan')
persediaan = ctrl.Antecedent(np.arange(0, 501, 1), 'persediaan')

# Variabel output
produksi = ctrl.Consequent(np.arange(0, 6001, 1), 'produksi', defuzzify_method='mom')

# Fungsi keanggotaan untuk variabel input
permintaan['rendah'] = fuzz.trimf(permintaan.universe, [0, 0, 2500])
permintaan['tinggi'] = fuzz.trimf(permintaan.universe, [2500, 5000, 5000])

persediaan['sedikit'] = fuzz.trimf(persediaan.universe, [0, 0, 250])
persediaan['banyak'] = fuzz.trimf(persediaan.universe, [250, 500, 500])

# Fungsi keanggotaan untuk variabel output
produksi['rendah'] = fuzz.trimf(produksi.universe, [0, 0, 3000])
produksi['tinggi'] = fuzz.trimf(produksi.universe, [0, 6000, 6000])

# Menentukan aturan fuzzy
aturan1 = ctrl.Rule(permintaan['rendah'] & persediaan['banyak'], produksi['rendah'])
aturan2 = ctrl.Rule(permintaan['rendah'] & persediaan['sedikit'], produksi['rendah'])
aturan3 = ctrl.Rule(permintaan['tinggi'] & persediaan['banyak'], produksi['tinggi'])
aturan4 = ctrl.Rule(permintaan['tinggi'] & persediaan['sedikit'], produksi['tinggi'])

# Membuat kontrol sistem fuzzy
fuzzy_control = ctrl.ControlSystem([aturan1, aturan2, aturan3, aturan4])

# Simulasi kontrol sistem fuzzy
fuzzy_simulation = ctrl.ControlSystemSimulation(fuzzy_control)

# Memasukkan input ke dalam kontrol sistem
fuzzy_simulation.input['permintaan'] = 3000
fuzzy_simulation.input['persediaan'] = 400

# Menghitung produksi
fuzzy_simulation.compute()

# Menampilkan hasil produksi
print("Jumlah unit mobil jenis XYZ yang harus diproduksi:", fuzzy_simulation.output['produksi'])

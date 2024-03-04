# Import library yang diperlukan
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Variabel input
demand = ctrl.Antecedent(np.arange(0, 5000, 1), 'demand')
inventory = ctrl.Antecedent(np.arange(0, 500, 1), 'inventory')

# Variabel output
production = ctrl.Consequent(np.arange(0, 6000, 1), 'production')

# Fungsi keanggotaan untuk variabel input
demand['low'] = fuzz.trimf(demand.universe, [0, 0, 2500])
demand['high'] = fuzz.trimf(demand.universe, [2500, 5000, 5000])

inventory['low'] = fuzz.trimf(inventory.universe, [0, 0, 250])
inventory['high'] = fuzz.trimf(inventory.universe, [250, 500, 500])

# Fungsi keanggotaan untuk variabel output
production['low'] = fuzz.trimf(production.universe, [0, 0, 3000])
production['high'] = fuzz.trimf(production.universe, [0, 6000, 6000])

# Menentukan aturan fuzzy
rule1 = ctrl.Rule(demand['low'] & inventory['high'], production['low'])
rule2 = ctrl.Rule(demand['low'] & inventory['low'], production['low'])
rule3 = ctrl.Rule(demand['high'] & inventory['high'], production['high'])
rule4 = ctrl.Rule(demand['high'] & inventory['low'], production['high'])

# Membuat kontrol sistem fuzzy
production_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4])

# Simulasi kontrol sistem fuzzy
production_calculation = ctrl.ControlSystemSimulation(production_ctrl)

# Memasukkan input ke dalam kontrol sistem
production_calculation.input['demand'] = 3000
production_calculation.input['inventory'] = 400

# Menghitung produksi
production_calculation.compute()

# Menampilkan hasil produksi
print("Jumlah unit mobil jenis XYZ yang harus diproduksi:", production_calculation.output['production'])

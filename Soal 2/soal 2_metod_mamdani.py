import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define input variables
demand = ctrl.Antecedent(np.arange(0, 5000, 1), 'demand')
inventory = ctrl.Antecedent(np.arange(0, 500, 1), 'inventory')

# Define output variable
production = ctrl.Consequent(np.arange(0, 5000, 1), 'production')

# Define membership functions for input variables
demand['turun'] = fuzz.trimf(demand.universe, [1000, 1000, 2500])
demand['naik'] = fuzz.trimf(demand.universe, [1000, 2500, 4000])
demand['tinggi'] = fuzz.trimf(demand.universe, [2500, 4000, 5000])

inventory['sedikit'] = fuzz.trimf(inventory.universe, [100, 100, 250])
inventory['banyak'] = fuzz.trimf(inventory.universe, [100, 250, 400])
inventory['tinggi'] = fuzz.trimf(inventory.universe, [250, 500, 500])

# Define membership functions for output variable
production['berkurang'] = fuzz.trimf(production.universe, [0, 0, 1500])
production['konstan'] = fuzz.trimf(production.universe, [1000, 1500, 4000])
production['bertambah'] = fuzz.trimf(production.universe, [2500, 5000, 5000])

# Define fuzzy rules
rule1 = ctrl.Rule(demand['turun'] & inventory['banyak'], production['berkurang'])
rule2 = ctrl.Rule(demand['turun'] & inventory['sedikit'], production['berkurang'])
rule3 = ctrl.Rule(demand['naik'] & inventory['banyak'], production['bertambah'])
rule4 = ctrl.Rule(demand['naik'] & inventory['sedikit'], production['bertambah'])
# Create control system
production_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4])
production_simulation = ctrl.ControlSystemSimulation(production_ctrl)

# Input values (demand and inventory)
production_simulation.input['demand'] = 3000  # Permintaan bulan ini
production_simulation.input['inventory'] = 300  # Persediaan di gudang

# Compute production
production_simulation.compute()

# Output production
print("Recommended production level:", production_simulation.output['production'])


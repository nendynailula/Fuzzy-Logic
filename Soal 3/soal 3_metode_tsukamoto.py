# Import library yang diperlukan
import numpy as np

# Fungsi keanggotaan untuk variabel input
def fuzzy_input_demand(demand):
    demand_low = max(0, (2000 - demand) / 2000)
    demand_high = max(0, (demand - 2000) / 2000)
    return demand_low, demand_high

def fuzzy_input_inventory(inventory):
    inventory_low = max(0, (200 - inventory) / 500)
    inventory_high = max(0, (inventory - 200) / 500)
    return inventory_low, inventory_high

# Fungsi keanggotaan untuk variabel output
def fuzzy_output_production(production):
    if production <= 3000:
        production_low = 1
        production_high = 0
    else:
        production_low = max(0, (6000 - production) / 3000)
        production_high = max(0, (production - 3000) / 3000)
    return production_low, production_high

# Fungsi Tsukamoto
def tsukamoto(demand, inventory):
    demand_low, demand_high = fuzzy_input_demand(demand)
    inventory_low, inventory_high = fuzzy_input_inventory(inventory)
    
    # Rule Evaluation
    rule1 = min(demand_low, inventory_high)
    rule2 = min(demand_low, inventory_low)
    rule3 = min(demand_high, inventory_high)
    rule4 = min(demand_high, inventory_low)

    # Inference
    production = (rule1 * 3000 + rule2 * 3000 + rule3 * 6000 + rule4 * 6000) / (rule1 + rule2 + rule3 + rule4)

    return production

# Permintaan dan Persediaan
demand = 3000
inventory = 400

# Memanggil fungsi Tsukamoto
production = tsukamoto(demand, inventory)
print("Jumlah unit mobil jenis XYZ yang harus diproduksi:", production)

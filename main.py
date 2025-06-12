# main.py
import pandas as pd
import re

# File input
FILE1 = "annotated_cells_with_probabilities_Exp5_1.txt"
FILE2 = "12_05_2025_DAPI_all_data_weight.txt"
OUTPUT = "12_05_2025_DAPI_all_data_weight_partialoutput.txt"

# Carica i due file con separatore doppio spazio
df1 = pd.read_csv(FILE1, sep=r"\s{2,}", engine="python")
df2 = pd.read_csv(FILE2, sep=r"\s{2,}", engine="python")

# Filtra df2 per righe che iniziano per 'Exp5'
df2_filtered = df2[df2.iloc[:, 0].astype(str).str.startswith("Exp5")].copy()

# Verifica che colonne necessarie siano presenti
required_cols = ['Time', 'V450-A']
for col in required_cols:
    if col not in df1.columns or col not in df2_filtered.columns:
        raise ValueError(f"Colonna '{col}' non trovata in uno dei file.")

# Esegui join su 'Time' e 'V450-A'
df_merged = pd.merge(
    df2_filtered,
    df1[['Time', 'V450-A', 'G1', 'S', 'G2']],
    on=['Time', 'V450-A'],
    how='inner'
)

# Scrivi il risultato con doppio spazio come separatore
df_merged.to_csv(OUTPUT, sep='  ', index=False)
print(f"File generato: {OUTPUT}")

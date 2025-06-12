# Exp5 Data Filter Script

Questo script confronta due file (`annotated_cells_with_probabilities_Exp5_1.txt` e `12_05_2025_DAPI_all_data_weight.txt`) ed estrae solo le righe dove:

- Il nome dell’esperimento comincia con `Exp5`
- I valori delle colonne `Time` e `V450-A` coincidono in entrambi i file

## Output
Crea un file `12_05_2025_DAPI_all_data_weight_partialoutput.txt` che contiene:
- La riga completa dal secondo file (`DAPI`)
- Più le colonne `G1`, `S`, `G2` dal primo file (`annotated`)

## Uso

1. Assicurati di avere Python 3 e `pandas` installato:
   ```bash
   pip install pandas

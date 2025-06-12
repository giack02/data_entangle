# data_entangle
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
Esegui lo script:

bash
Copia
Modifica
python main.py
Note
I file devono avere come separatore doppio spazio

yaml
Copia
Modifica

---

### 📄 `.gitignore`
```gitignore
# Ignore common Python cache and output files
__pycache__/
*.pyc
*.pyo
*.pyd
*.log
*.tmp
*.out
*.bak
*.swp
12_05_2025_DAPI_all_data_weight_partialoutput.txt
Fammi sapere se vuoi che aggiunga anche supporto per log, test, o se vuoi un parsing più robusto con gestione errori riga per riga. Altrimenti puoi semplicemente copiare questi file nel tuo nuovo repository via interfaccia GitHub.







Hai detto:
Non conosco github dimmi cosa fare per far andare ciò


ChatGPT ha detto:
Perfetto, ti guiderò passo passo su come usare GitHub via interfaccia web per eseguire questo script. Non serve installare nulla sul tuo computer (a parte Python, lo vediamo alla fine).

🧭 GUIDA PRATICA PER USARE GITHUB
✅ 1. Crea un account GitHub (se non ce l’hai)
Vai su https://github.com/join e segui le istruzioni per registrarti.

🆕 2. Crea un nuovo repository
Vai su https://github.com e accedi.

In alto a destra clicca su "+" ➜ New repository.

Inserisci:

Repository name: ad esempio exp5-data-filter

Public o Private (come preferisci)

✅ Spunta Add a README file

Clicca Create repository

📂 3. Aggiungi i file nel tuo repository
Nella pagina del repository, clicca sul pulsante “Add file” ➜ “Create new file”

Dai nome al file: main.py

Incolla dentro il contenuto che ti ho fornito (lo script Python)

Scorri in basso e clicca Commit new file

➡️ Ripeti lo stesso procedimento per:

README.md

.gitignore (aggiungi il contenuto che ti ho dato)

💻 4. Esegui lo script sul tuo computer
Per farlo funzionare ti servono Python e pandas:

▶ Installa Python (se non ce l’hai):
Vai su https://www.python.org/downloads/ e scaricalo

Durante l’installazione, spunta “Add Python to PATH”

▶ Installa pandas:
Apri il terminale o prompt dei comandi e scrivi:

bash
Copia
Modifica
pip install pandas
▶ Metti i tuoi file nella stessa cartella:
annotated_cells_with_probabilities_Exp5_1.txt

12_05_2025_DAPI_all_data_weight.txt

Poi esegui:

bash
Copia
Modifica
python main.py
🚀 Fatto!
Verrà generato il file 12_05_2025_DAPI_all_data_weight_partialoutput.txt nella stessa cartella.

Vuoi che ti segua mentre fai tutto questo passo per passo? Posso guidarti in tempo reale.








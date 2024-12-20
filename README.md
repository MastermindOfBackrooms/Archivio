# Backrooms Research Tools
Creato da Jashin L

## Descrizione
Una suite di strumenti per la ricerca e documentazione delle Backrooms, che include un traduttore automatico e un database per la gestione dei report.

## Tools Disponibili

### 1. Traduttore (translator.py)
Un tool per tradurre e archiviare testi in italiano.

Funzionalità:
- Traduzione automatica in italiano
- Salvataggio progressivo dei file (1.txt, 2.txt, etc.)
- Archivio organizzato nella cartella "traduzioni"
- Lettura dei file tradotti
- Elenco delle traduzioni disponibili

### 2. Database (database.py)
Sistema di gestione per i report delle Backrooms.

Funzionalità:
- Creazione di nuovi report
- Template predefinito per la documentazione
- Numerazione automatica dei report
- Visualizzazione dell'archivio
- Lettura dei report esistenti
- Modifica dei report salvati
- Data e ora automatiche per ogni entry

## Requisiti
- Python 3.x
- googletrans==3.1.0a0

## Installazione
pip install googletrans==3.1.0a0

Utilizzo
Avvio Traduttore:
python3 translator.py

Avvio Database:
python3 database.py

Struttura Directory
backrooms-tools/
├── translator.py
├── database.py
├── traduzioni/
└── backrooms_database/

Note
Utilizzare Ctrl+D per terminare l'input nei campi di testo
I file vengono salvati automaticamente nelle rispettive cartelle
Ogni report include timestamp automatico

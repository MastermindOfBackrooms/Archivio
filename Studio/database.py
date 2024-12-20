import os
from datetime import datetime

class BackroomsDB:
    def __init__(self):
        self.db_folder = "backrooms_database"
        if not os.path.exists(self.db_folder):
            os.makedirs(self.db_folder)

    def get_next_file_number(self):
        files = os.listdir(self.db_folder)
        numbers = [int(f.split('.')[0]) for f in files if f.endswith('.txt')]
        return max(numbers, default=0) + 1

    def create_entry(self):
        print("\n=== Nuovo Report Backrooms ===")
        print("Inserisci le informazioni (premi Ctrl+D per salvare):")
        print("\nTemplate suggerito:")
        print("Livello:")
        print("Classe di Sicurezza:")
        print("Entità presenti:")
        print("Descrizione:")
        print("\nInserisci il tuo testo:")
        
        content = ""
        try:
            while True:
                line = input()
                content += line + "\n"
        except EOFError:
            if content.strip():
                file_num = self.get_next_file_number()
                filename = f"{self.db_folder}/{file_num}.txt"
                
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(f"Report #{file_num}\n")
                    f.write(f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n")
                    f.write("="*50 + "\n")
                    f.write(content)
                
                print(f"\nReport salvato in: {filename}")

    def list_entries(self):
        files = sorted([f for f in os.listdir(self.db_folder) if f.endswith('.txt')],
                      key=lambda x: int(x.split('.')[0]))
        
        if not files:
            print("\nNessun report presente")
            return []
        
        print("\nElenco Reports:")
        for i, file in enumerate(files, 1):
            print(f"{i}. Report {file}")
        return files

    def read_entry(self):
        files = self.list_entries()
        if not files:
            return
        
        while True:
            choice = input("\nInserisci il numero del report da leggere (0 per tornare indietro): ")
            if choice == "0":
                return
            try:
                file_index = int(choice) - 1
                if 0 <= file_index < len(files):
                    filename = f"{self.db_folder}/{files[file_index]}"
                    with open(filename, 'r', encoding='utf-8') as f:
                        content = f.read()
                    print("\n" + "="*50)
                    print(content)
                    print("="*50)
                    input("\nPremi Enter per continuare...")
                    break
                else:
                    print("Numero non valido!")
            except ValueError:
                print("Inserisci un numero valido!")

    def edit_entry(self):
        files = self.list_entries()
        if not files:
            return
        
        while True:
            choice = input("\nInserisci il numero del report da modificare (0 per tornare indietro): ")
            if choice == "0":
                return
            try:
                file_index = int(choice) - 1
                if 0 <= file_index < len(files):
                    filename = f"{self.db_folder}/{files[file_index]}"
                    
                    # Leggi il contenuto attuale
                    with open(filename, 'r', encoding='utf-8') as f:
                        old_content = f.read()
                    print("\nContenuto attuale:")
                    print("="*50)
                    print(old_content)
                    print("="*50)
                    
                    # Modifica
                    print("\nInserisci il nuovo contenuto (premi Ctrl+D per salvare):")
                    new_content = ""
                    try:
                        while True:
                            line = input()
                            new_content += line + "\n"
                    except EOFError:
                        if new_content.strip():
                            with open(filename, 'w', encoding='utf-8') as f:
                                f.write(f"Report #{file_index + 1}\n")
                                f.write(f"Data ultima modifica: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n")
                                f.write("="*50 + "\n")
                                f.write(new_content)
                            print(f"\nReport modificato con successo!")
                    break
                else:
                    print("Numero non valido!")
            except ValueError:
                print("Inserisci un numero valido!")

def show_menu():
    db = BackroomsDB()
    while True:
        print("\n=== Database Backrooms ===")
        print("Crediti: Jashin L")
        print("1. Nuovo Report")
        print("2. Elenco Reports")
        print("3. Leggi Report")
        print("4. Modifica Report")
        print("5. Esci")
        
        choice = input("\nScegli un'opzione (1-5): ")
        
        if choice == "1":
            db.create_entry()
        elif choice == "2":
            db.list_entries()
        elif choice == "3":
            db.read_entry()
        elif choice == "4":
            db.edit_entry()
        elif choice == "5":
            print("\nDatabase chiuso con successo!")
            break
        else:
            print("\nOpzione non valida!")

if __name__ == "__main__":
    show_menu()

from googletrans import Translator
import os

def create_translations_folder():
    if not os.path.exists("traduzioni"):
        os.makedirs("traduzioni")

def get_next_file_number():
    files = os.listdir("traduzioni")
    numbers = [int(f.split('.')[0]) for f in files if f.endswith('.txt')]
    return max(numbers, default=0) + 1

def translate_and_save(text):
    translator = Translator()
    translation = translator.translate(text, dest='it')
    
    file_number = get_next_file_number()
    filename = f"traduzioni/{file_number}.txt"
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("TESTO ORIGINALE:\n")
        f.write(text + "\n\n")
        f.write("TRADUZIONE:\n")
        f.write(translation.text)
    
    print(f"\nTraduzione salvata in: {filename}")
    return translation.text

def list_translations():
    if not os.path.exists("traduzioni"):
        print("\nNessuna traduzione presente")
        return []
    
    files = sorted([f for f in os.listdir("traduzioni") if f.endswith('.txt')],
                  key=lambda x: int(x.split('.')[0]))
    
    if not files:
        print("\nNessuna traduzione presente")
        return []
    
    print("\nElenco traduzioni:")
    for i, file in enumerate(files, 1):
        print(f"{i}. File {file}")
    return files

def read_translation_file():
    files = list_translations()
    if not files:
        return
    
    while True:
        choice = input("\nInserisci il numero del file da leggere (0 per tornare indietro): ")
        if choice == "0":
            return
        try:
            file_index = int(choice) - 1
            if 0 <= file_index < len(files):
                filename = f"traduzioni/{files[file_index]}"
                with open(filename, 'r', encoding='utf-8') as f:
                    content = f.read()
                print(f"\nContenuto del file {files[file_index]}:")
                print("="*50)
                print(content)
                print("="*50)
                input("\nPremi Enter per continuare...")
                break
            else:
                print("Numero non valido!")
        except ValueError:
            print("Inserisci un numero valido!")

def show_menu():
    while True:
        print("\n=== Traduttore Backrooms ===")
        print("Crediti: Jashin L")
        print("1. Nuova traduzione")
        print("2. Elenco files")
        print("3. Leggi traduzione")
        print("4. Esci")
        
        choice = input("\nScegli un'opzione (1-4): ")
        
        if choice == "1":
            print("\nIncolla il testo da tradurre (premi Ctrl+D quando hai finito):")
            text = ""
            try:
                while True:
                    line = input()
                    text += line + "\n"
            except EOFError:
                if text:
                    translated = translate_and_save(text.strip())
                    print("\nTraduzione:")
                    print(translated)
        
        elif choice == "2":
            list_translations()
        
        elif choice == "3":
            read_translation_file()
        
        elif choice == "4":
            print("\nGrazie per aver usato il traduttore!")
            break
        
        else:
            print("\nOpzione non valida!")

if __name__ == "__main__":
    create_translations_folder()
    show_menu()

import json
import os

# Chiavi da rimuovere da ogni oggetto JSON
KEYS_TO_REMOVE = {"link", "latitudine", "longitudine"}


def remove_keys(data, keys):
    """Rimuove ricorsivamente le chiavi specificate da dizionari e liste."""
    if isinstance(data, dict):
        return {
            key: remove_keys(value, keys)
            for key, value in data.items()
            if key not in keys
        }
    elif isinstance(data, list):
        return [remove_keys(item, keys) for item in data]
    else:
        return data


def process_directory(directory_path):
    """Scansiona tutti i file .json nella cartella ed elimina le chiavi desiderate."""
    if not os.path.exists(directory_path):
        print(f"Errore: La cartella '{directory_path}' non esiste.")
        return

    for filename in os.listdir(directory_path):
        if filename.endswith(".json"):
            file_path = os.path.join(directory_path, filename)

            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = json.load(f)

                # Rimuove le chiavi definite
                cleaned_content = remove_keys(content, KEYS_TO_REMOVE)

                # Salva il file modificato mantenendo la formattazione con rientro a 2 spazi
                with open(file_path, "w", encoding="utf-8") as f:
                    json.dump(cleaned_content, f, ensure_ascii=False, indent=2)

                print(f"Completato: {filename}")

            except Exception as e:
                print(f"Errore durante l'elaborazione di {filename}: {e}")


if __name__ == "__main__":
    folder_path = input("Inserisci il percorso della cartella contenente i file JSON: ").strip()
    process_directory(folder_path)
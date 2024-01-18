import subprocess

def install_requirements(requirements_file='requirements.txt'):
    try:
        with open(requirements_file, 'r') as file:
            modules = file.readlines()
        modules = [module.strip() for module in modules if module.strip()]

        if not modules:
            print("Plik 'requirements.txt' jest pusty lub nie zawiera żadnych modułów do zainstalowania.")
            return

        print(f"Instalowanie modułów z {requirements_file}...")
        subprocess.call(["pip", "install"] + modules)
        print("Instalacja zakończona.")

    except FileNotFoundError:
        print(f"Plik {requirements_file} nie został znaleziony.")

if __name__ == "__main__":
    install_requirements()

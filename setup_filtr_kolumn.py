import requests
import zipfile
import io
import os
import shutil

def download_and_extract(repo_url, target_folder):
    response = requests.get(repo_url)
    if response.status_code == 200:
        with zipfile.ZipFile(io.BytesIO(response.content)) as z:
            temp_dir = 'temp_extracted'
            z.extractall(temp_dir)
            extracted_folder = os.path.join(temp_dir, os.listdir(temp_dir)[0])

            if not os.path.exists(target_folder):
                os.makedirs(target_folder)

            for item in os.listdir(extracted_folder):
                shutil.move(os.path.join(extracted_folder, item), target_folder)

            shutil.rmtree(temp_dir)
        print(f"Pliki pobrano z {repo_url} i przeniesiono do {target_folder}.")
    else:
        print(f"Błąd podczas pobierania: {response.status_code}")

def main():
    filtr_kolumn_repo_url = "https://github.com/pkonieczny007/filtr_kolum_EXCEL/archive/refs/heads/main.zip"
    filtr_kolumn_folder = "Filtr_Kolumn"
    download_and_extract(filtr_kolumn_repo_url, filtr_kolumn_folder)

    setup_folder = os.path.join(filtr_kolumn_folder, 'setup')
    os.makedirs(setup_folder, exist_ok=True)
    script_name = os.path.basename(__file__)
    shutil.copy(script_name, os.path.join(setup_folder, script_name))
    print(f"Plik {script_name} został skopiowany do {os.path.join(setup_folder, script_name)}.")

if __name__ == "__main__":
    main()

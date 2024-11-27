import os
import requests

# İndirme klasörünü belirleyin
output_folder = r"D:\Belgelerim\Desktop\chelsa\tasmax"
os.makedirs(output_folder, exist_ok=True)

# Yıl ve ay aralıklarını belirleyin
years = range(1979, 2019)  # Örneğin 1979'dan 2020'ye kadar
months = range(1, 13)

# Temel URL
base_url = "https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/monthly/tasmax/"

# Dosyaları indirin
for year in years:
    for month in months:
        # Dosya adı ve URL oluşturun
        month_str = f"{month:02d}"  # Ayı iki basamaklı yapın
        file_name = f"CHELSA_tasmax_{year}_{month_str}_V.2.1.tif"
        url = base_url + file_name

        # Çıkış dosya yolu
        output_path = os.path.join(output_folder, file_name)

        # Dosya zaten mevcutsa atlayın
        if os.path.exists(output_path):
            print(f"Zaten mevcut: {file_name}")
            continue

        # Dosyayı indirin
        print(f"İndiriliyor: {file_name}")
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(output_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            print(f"İndirildi: {file_name}")
        else:
            print(f"İndirilemedi: {file_name}")

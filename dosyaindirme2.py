import os
import requests

# İndirme klasörü
output_folder = r"D:\Belgelerim\Desktop\chelsa\tasmin"  # İndirilecek dosyaların kaydedileceği klasör
os.makedirs(output_folder, exist_ok=True)

# URL dosyasını yükleyin
url_file = r"D:\Belgelerim\Desktop\chelsa\tasmin.txt"  # Dosyanızın tam yolu

# URL listesini oku ve indir
with open(url_file, "r") as file:
    urls = file.readlines()

for url in urls:
    url = url.strip()  # Satır başı ve sonundaki boşlukları sil
    if not url:  # Boş satırları atla
        continue
    
    file_name = os.path.basename(url)  # Dosya adını URL'den çıkar
    output_path = os.path.join(output_folder, file_name)
    
    if os.path.exists(output_path):
        print(f"Zaten mevcut: {file_name}")
        continue
    
    print(f"İndiriliyor: {file_name}")
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # HTTP hatalarını kontrol et
        with open(output_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"Tamamlandı: {file_name}")
    except Exception as e:
        print(f"İndirme hatası ({file_name}): {e}")

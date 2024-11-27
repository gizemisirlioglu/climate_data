import os
import shutil

# Ana klasör yolunu belirtin
tasmin_folder = r"D:\Belgelerim\Desktop\chelsa\tasmax"

# Dosyaları listele
files = [f for f in os.listdir(tasmin_folder) if f.endswith(".tif")]

# Her dosyayı işle
for file_name in files:
    # Dosya adından yılı çıkar
    parts = file_name.split("_")  # "CHELSA_tasmin_01_1980_V.2.1.tif" -> ['CHELSA', 'tasmin', '01', '1980', 'V.2.1.tif']
    year = parts[3]  # Yıl "1980" kısmı
    
    # Yıl klasörünün yolunu oluştur
    year_folder = os.path.join(tasmin_folder, year)
    
    # Yıl klasörü yoksa oluştur
    if not os.path.exists(year_folder):
        os.makedirs(year_folder)
    
    # Dosyayı ilgili yıl klasörüne taşı
    src_path = os.path.join(tasmin_folder, file_name)
    dst_path = os.path.join(year_folder, file_name)
    shutil.move(src_path, dst_path)

    print(f"{file_name} -> {year}/")

print("Dosyalar başarıyla taşındı!")

import os
from osgeo import gdal

# Ana giriş klasörü ve çıkış klasörü
input_base_folder = r"D:\Belgelerim\Desktop\chelsa\tasmin"
output_base_folder = r"D:\Belgelerim\Desktop\chelsa\tasmin\ortalamalar_min"

# Çıkış klasörünü oluştur
if not os.path.exists(output_base_folder):
    os.makedirs(output_base_folder)

# Yıl aralığını belirle
start_year = 1979
end_year = 2019

# Tüm yıllar için işlemi tekrarla
for year in range(start_year, end_year + 1):
    input_folder = os.path.join(input_base_folder, str(year))
    output_file = os.path.join(output_base_folder, f"{year}average.tif")

    # Klasördeki tüm TIFF dosyalarını topla
    if not os.path.exists(input_folder):
        print(f"{year} yılı için klasör bulunamadı: {input_folder}")
        continue

    tiff_files = [os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.endswith(".tif")]
    if not tiff_files:
        print(f"{year} yılı için TIFF dosyası bulunamadı: {input_folder}")
        continue

    # GDAL Virtual Raster (.vrt) oluştur
    vrt_file = os.path.join(input_folder, "temp.vrt")
    try:
        gdal.BuildVRT(vrt_file, tiff_files)

        # Ortalamayı hesapla ve kaydet
        gdal.Translate(output_file, vrt_file, format="GTiff", creationOptions=["COMPRESS=LZW"])
        print(f"{year} yılı için ortalama raster oluşturuldu: {output_file}")
    except Exception as e:
        print(f"{year} yılı için işlem sırasında hata oluştu: {e}")
    finally:
        # Geçici VRT dosyasını sil
        if os.path.exists(vrt_file):
            os.remove(vrt_file)

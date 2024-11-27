import os
from osgeo import gdal

# Giriş klasörü ve çıkış dosya yolu
input_folder = r"D:\Belgelerim\Desktop\worldclim\ortalama"
output_file = r"D:\Belgelerim\Desktop\worldclim\ortalama\ortalama.tif"

# Klasördeki tüm TIFF dosyalarını topla
tiff_files = [os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.endswith(".tif")]

# GDAL Virtual Raster (.vrt) oluştur
vrt_file = os.path.join(input_folder, "temp.vrt")
gdal.BuildVRT(vrt_file, tiff_files)

# Ortalamayı hesapla ve kaydet
gdal.Translate(output_file, vrt_file, format="GTiff", creationOptions=["COMPRESS=LZW"])

print(f"Ortalama raster oluşturuldu: {output_file}")

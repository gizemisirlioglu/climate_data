import os
from osgeo import gdal

input_base_folder = r"data_set"
output_base_folder = r"output_folder"

if not os.path.exists(output_base_folder):
    os.makedirs(output_base_folder)

start_year = 1979
end_year = 2019

for year in range(start_year, end_year + 1):
    input_folder = os.path.join(input_base_folder, str(year))
    output_file = os.path.join(output_base_folder, f"{year}average.tif")

    if not os.path.exists(input_folder):
        print(f"{year} folder not found for year: {input_folder}")
        continue

    tiff_files = [os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.endswith(".tif")]
    if not tiff_files:
        print(f"{year} no TIFF file found for the year: {input_folder}")
        continue

    vrt_file = os.path.join(input_folder, "temp.vrt")
    try:
        gdal.BuildVRT(vrt_file, tiff_files)

        gdal.Translate(output_file, vrt_file, format="GTiff", creationOptions=["COMPRESS=LZW"])
        print(f"{year} Created average raster for the year: {output_file}")
    except Exception as e:
        print(f"{year} error occurred during processing for the year: {e}")
    finally:
        if os.path.exists(vrt_file):
            os.remove(vrt_file)

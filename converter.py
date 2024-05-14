
# Import Module  
import tabula
import os
  
# Read PDF File 
# this contain a list 
file_path = r"C:\Users\David\Downloads\Phase 3\roofing_tbl.pdf"
output_directory = r"C:\Users\David\Downloads\Phase 3\excel"

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

output_excel_filename = "roofing.csv"

output_excel_path = os.path.join(output_directory, output_excel_filename)

tabula.convert_into(file_path, output_excel_path, output_format="csv", pages='all')

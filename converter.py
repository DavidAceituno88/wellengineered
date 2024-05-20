
# Import Module  
import tabula
import os
from os import listdir
from os.path import isfile, join


dirpath= "C:\\Users\\David\\Downloads\\Phase 3\\originals\\"
#file_path = r"C:\Users\David\Downloads\Phase 3\roofing_tbl.pdf"
output_directory = r"C:\Users\David\Downloads\Phase 3\excel"

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

files = [f for f in listdir(dirpath) if isfile(join(dirpath, f))]

print(files)

#Extracting the file name
sub1 = "C:\\Users\\David\\Downloads\\Phase 3\\originals\\"
sub2 = ".pdf"

# getting elements in between using split() and join()
for file_path in files:
    sub1 = "C:\\Users\\David\\Downloads\\Phase 3\\originals\\"
    sub2 = ".pdf"
    file_name = ''.join(file_path.split(sub2)[0])
    file_name=  file_name +'.csv'
    output_excel_path = os.path.join(output_directory, file_name)
    tabula.convert_into(file_path, output_excel_path, output_format="csv", pages='all')



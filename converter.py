
# Import Module  
import tabula
  
# Read PDF File 
# this contain a list 
file_path = r"C:\Users\David\Downloads\Phase 3\roofing_tbl.pdf"
destination_folter = r"C:\Users\David\Downloads\Phase 3"
df = tabula.read_pdf(file_path, pages ='all')[0] 
  

import os
import shutil
from datetime import datetime

root_dir = 'C:\\Users\\franc\\OneDrive\\Documentos\\Devlopment\\Python Impressionador'
destination_dir = 'C:\\Users\\franc\\Downloads\\Destino'

dir = destination_dir
for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))


for subdir, dirs, files in os.walk(root_dir):
    files = [f for f in files if os.path.getsize(os.path.join(subdir, f)) > 0]
    latest_file = max(files, key=lambda x: os.path.getmtime(os.path.join(subdir, x)))
    latest_file_path = os.path.join(subdir, latest_file)
    print(latest_file)
    shutil.copy2(latest_file_path, destination_dir)
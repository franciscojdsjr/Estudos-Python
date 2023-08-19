import os
import csv
import re
from datetime import datetime
from shutil import copy2

# Define the root directory to search for folders
root_dir = 'C:\\Users\\franc\\Downloads\\Bases'

# Define the destination folder
destination_folder = 'C:\\Users\\franc\\Downloads\\Destino'

# Define the new delimiter
new_delimiter = '&'

# Iterate through all the subdirectories in the root directory
for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        # Check if the file is a CSV file and its size is above 0KB
        if file.endswith('.csv') and os.path.getsize(os.path.join(subdir, file)) > 0:
            # Get the modification time of the file
            file_time = os.path.getmtime(os.path.join(subdir, file))
            file_datetime = datetime.fromtimestamp(file_time)
            # check the latest file
            if not 'latest_csv' in locals() or file_datetime > latest_csv[1]:
                latest_csv = (os.path.join(subdir, file), file_datetime)

# if there is any csv file
if 'latest_csv' in locals():
    # Open the file and change the delimiter
    with open(latest_csv[0], 'r', newline='', errors='ignore') as csv_file, open(destination_folder + '/' + os.path.basename(latest_csv[0]), 'w', newline='') as new_csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';',lineterminator='\n', quotechar='"', quoting=csv.QUOTE_ALL)
        csv_writer = csv.writer(new_csv_file, delimiter=new_delimiter,lineterminator='\n', quotechar='"', quoting=csv.QUOTE_ALL)
        for row in csv_reader:
            new_row = [field.strip() if field.startswith('"') and field.endswith('"') else field for field in row]
            csv_writer.writerow(new_row)
            
            

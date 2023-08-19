import csv
import pathlib
from datetime import datetime


# Define the root directory to search for folders
root_dir = pathlib.Path('C:\\Users\\franc\\Downloads\\Bases')

# Define the destination folder
destination_folder = pathlib.Path('C:\\Users\\franc\\Downloads\\Destino')

# Define the new delimiter
new_delimiter = '&'

# Keep track of the latest CSV file found
latest_csv = None

# Iterate through all the files in the root directory
for file in root_dir.glob('**/*.csv'):
    # Check if the file is not empty
    if file.stat().st_size > 0:
        # Get the modification time of the file
        file_time = file.stat().st_mtime
        file_datetime = datetime.fromtimestamp(file_time)
        # Check if this is the latest CSV file found
        if not latest_csv or file_datetime > latest_csv[1]:
            latest_csv = (file, file_datetime)

# If there is a CSV file, change the delimiter
if latest_csv:
    with latest_csv[0].open('r', newline='', errors='ignore') as csv_file, (destination_folder / latest_csv[0].name).open('w', newline='') as new_csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        csv_writer = csv.writer(new_csv_file, delimiter=new_delimiter)
        # Check if the CSV file has a header
        header = next(csv_reader, None)
        if header is not None:
            csv_writer.writerow(header)
        # Write the rows with the new delimiter
        for row in csv_reader:
            new_row = [field.strip() if field.startswith('"') and field.endswith('"') else field for field in row]
            csv_writer.writerow(new_row)

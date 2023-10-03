import os
import shutil

# Define the source directory where your files are located
source_dir = "/home/huzaifa/Desktop/Python Script"
file_extensions = {
    ".txt": "TextFiles",
    ".jpg": "Images",
    ".mp3": "Music",
    ".pdf": "PDFs",
    ".xlsx": "Spreadsheets",
    ".mp4": "Videos",
    ".zip": "Compressed",
}

# Define a folder for other/unknown file types
default_folder = "OtherFiles"

# Create folders for each category if they don't exist
for folder_name in file_extensions.values():
    folder_path = os.path.join(source_dir, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Iterate through files in the source directory and its subdirectories
for root, _, files in os.walk(source_dir):
    for filename in files:
        file_path = os.path.join(root, filename)
        
        # Check if it's a file (not a directory)
        if os.path.isfile(file_path):
            # Get the file extension
            file_extension = os.path.splitext(filename)[1].lower()

            # Check if the file extension is in the dictionary
            if file_extension in file_extensions:
                # Get the target folder name based on the file extension
                target_folder = file_extensions[file_extension]

                # Construct the full path to the target folder
                target_folder_path = os.path.join(source_dir, target_folder)

                # Move the file to the target folder
                shutil.move(file_path, os.path.join(target_folder_path, filename))

print("File organization complete.")

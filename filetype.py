import os

file_types = {
    ".txt": "TextFiles",
    ".jpg": "Images",
    ".mp3": "Music",
    ".pdf": "PDFs",
    ".xlsx": "Spreadsheets",
    ".mp4": "Videos",
    ".zip": "Compressed",
}

# Create 10 files for each file type in the current directory
for ext, folder in file_types.items():
    for i in range(1, 10):
        file_name = f"file_{i}{ext}"
        file_path = os.path.join(os.getcwd(), file_name)
        with open(file_path, "w") as file:
            file.write(f"This is a sample {ext} file {i}")

print("Files created successfully.")

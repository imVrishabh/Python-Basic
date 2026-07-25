import os

# Ask user for directory path
path = input("Enter directory path (or press Enter for current): ")

# Use current directory if user doesn't enter a path
if path == "":
    path = "."

try:
    # Get list of files and folders
    contents = os.listdir(path)
    
    print(f"Contents of '{path}':")
    for item in contents:
        print(item)

except FileNotFoundError:
    print("Error: Directory not found.")
except PermissionError:
    print("Error: Permission denied.")

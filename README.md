# Desktop File Organizer

This Python script organizes files on your desktop by their extensions into separate folders. It groups files with the same extension into a dedicated folder named after the extension type (e.g., "TXT files", "JPEG files").

## Overview

The script performs the following tasks:
1. **Lists Files on Desktop**: Retrieves all files from the desktop directory.
2. **Groups Files by Extension**: Organizes files into categories based on their extensions.
3. **Creates Folders and Moves Files**: Creates folders for each file extension and moves the corresponding files into these folders.

## Requirements

This script uses built-in Python libraries, so no additional packages are required. Ensure you have Python installed on your system.

## Script Details

### 1. Import Libraries

The script uses `os` for file and directory operations and `shutil` for moving files.

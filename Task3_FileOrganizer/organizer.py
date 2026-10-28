
import os
import shutil
from pathlib import Path

EXTENSION_MAP = {
    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".xls": "Documents",
    ".xlsx": "Documents",
    ".ppt": "Documents",
    ".pptx": "Documents",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".webp": "Images",
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".mov": "Videos",
    ".avi": "Videos",
    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",
    ".tar": "Archives",
    ".py": "Code",
    ".java": "Code",
    ".c": "Code",
    ".cpp": "Code",
    ".html": "Code",
    ".css": "Code",
    ".js": "Code"
}


def organize_files(folder_path):
    folder = Path(folder_path)

    if not folder.is_dir():
        print("Error: The specified folder does not exist.")
        return

    moved = 0
    skipped = 0
    errors = 0

    print("\n===== FILE ORGANIZER =====")
    print(f"Folder: {folder.resolve()}\n")

    try:
        entries = list(os.scandir(folder))
    except PermissionError:
        print("Error: Permission denied while reading the folder.")
        return

    for entry in entries:
        if not entry.is_file(follow_symlinks=False):
            continue

        source = Path(entry.path)
        category = EXTENSION_MAP.get(source.suffix.lower())

        if category is None:
            skipped += 1
            print(f"Skipped: {source.name} (unknown file type)")
            continue

        destination_folder = folder / category

        try:
            destination_folder.mkdir(exist_ok=True)
            destination = destination_folder / source.name

            if destination.exists():
                stem = source.stem
                suffix = source.suffix
                number = 1

                while destination.exists():
                    destination = destination_folder / f"{stem}_{number}{suffix}"
                    number += 1

            shutil.move(str(source), str(destination))
            moved += 1
            print(f"Moved: {source.name} -> {category}/")

        except (PermissionError, FileExistsError, OSError) as error:
            errors += 1
            print(f"Error moving {source.name}: {error}")

    print("\n===== EXECUTION SUMMARY =====")
    print(f"Files moved:   {moved}")
    print(f"Files skipped: {skipped}")
    print(f"Errors:        {errors}")
    print("Organization completed.")


if __name__ == "__main__":
    target_folder = input("Enter the folder path to organize: ").strip().strip('"')
    organize_files(target_folder)

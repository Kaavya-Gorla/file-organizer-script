import os
import shutil

def organize_folder(target_directory):
    # Dictionary to map folder names to extensions
    EXTENSIONS_MAPPING = {
        'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.svg'],
        'Audio': ['.mp3', '.wav', '.aac'],
        'Videos': ['.mp4', '.mkv', '.mov', '.avi'],
        'Archives': ['.zip', '.tar', '.gz', '.rar']
    }

    print(f"Scanning directory: {target_directory}")

    for filename in os.listdir(target_directory):
        file_path = os.path.join(target_directory, filename)

        # Ignore folders inside the directory
        if os.path.isdir(file_path):
            continue

        _, extension = os.path.splitext(filename)
        extension = extension.lower()

        moved = False
        for folder_name, extensions_list in EXTENSIONS_MAPPING.items():
            if extension in extensions_list:
                destination_folder = os.path.join(target_directory, folder_name)
                
                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)
                
                shutil.move(file_path, os.path.join(destination_folder, filename))
                print(f"Moved: {filename} -> {folder_name}/")
                moved = True
                break
        
        if not moved:
            print(f"Skipped format: {filename}")

if __name__ == "__main__":
    # Runs automatically on the local Downloads folder
    user_downloads_path = os.path.expanduser("~/Downloads")
    organize_folder(user_downloads_path)

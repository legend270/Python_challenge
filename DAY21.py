import os
import shutil
from collections import defaultdict

def organize_files(directory):
    """
    Organize files in the specified directory by their extensions.
    Creates subdirectories for each file type and moves files accordingly.
    """
    # Dictionary to map extensions to file lists
    extension_map = defaultdict(list)
    
    # Supported file types and their folders
    supported_types = {
        'Documents': ['.pdf', '.docx', '.txt', '.pptx', '.xlsx', '.csv'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
        'Audio': ['.mp3', '.wav', '.flac', '.aac'],
        'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
        'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
        'Code': ['.py', '.js', '.html', '.css', '.cpp', '.java'],
        'Executables': ['.exe', '.msi', '.dmg', '.app'],
    }
    
    # Create reverse mapping for quick lookup
    extension_to_category = {}
    for category, extensions in supported_types.items():
        for ext in extensions:
            extension_to_category[ext.lower()] = category
    
    # Scan the directory
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        
        # Skip directories
        if os.path.isdir(filepath):
            continue
        
        # Get file extension
        _, ext = os.path.splitext(filename)
        ext = ext.lower()  # Normalize to lowercase
        
        # Determine category
        category = extension_to_category.get(ext, 'Other')
        
        # Add to our mapping
        extension_map[category].append((filename, ext))
    
    # Create folders and move files
    for category, files in extension_map.items():
        # Create category folder if it doesn't exist
        category_path = os.path.join(directory, category)
        os.makedirs(category_path, exist_ok=True)
        
        # Move each file to its category folder
        for filename, ext in files:
            src = os.path.join(directory, filename)
            dest = os.path.join(category_path, filename)
            
            # Handle naming conflicts
            if os.path.exists(dest):
                base, _ = os.path.splitext(filename)
                counter = 1
                while True:
                    new_filename = f"{base}_{counter}{ext}"
                    new_dest = os.path.join(category_path, new_filename)
                    if not os.path.exists(new_dest):
                        dest = new_dest
                        break
                    counter += 1
            
            shutil.move(src, dest)
            print(f"Moved: {filename} -> {category}/{os.path.basename(dest)}")
    
    print("\nOrganization complete!")

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Organize files in a directory by their extensions.")
    parser.add_argument('directory', help="Directory to organize")
    parser.add_argument('--dry-run', action='store_true', 
                       help="Show what would be done without actually moving files")
    
    args = parser.parse_args()
    
    if not os.path.isdir(args.directory):
        print(f"Error: {args.directory} is not a valid directory")
        return
    
    if args.dry_run:
        print("Dry run mode - no files will be moved")
        # Implement dry run logic (similar but without actual moves)
        # This would just print what would happen
    else:
        organize_files(args.directory)

if __name__ == "__main__":
    main()
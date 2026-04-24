import random
import shutil
import argparse
from pathlib import Path

def get_user_choice(files: list[Path]) -> Path:
    print("\n--- ASCII Collection ---")
    for file in files:
        print(f"- {file.name}")
    
    while True:
        # 1. Changed prompt to ask for the exact name
        choice = input("\nEnter exact file name: ").strip() + ".txt"
        
        # 2. Changed matching logic to require an exact match
        matches = [f for f in files if choice == f.name]
        
        # 3. Simplified the validation logic (no multiple matches possible)
        if len(matches) == 1:
            return matches[0]
        else:
            print("Exact file name not found. Please try again.")

def main():
    # Setup Argument Parser for CMD usage
    parser = argparse.ArgumentParser(description="Update Fastfetch ASCII via CMD")
    
    # Mutually exclusive group: You can't be random AND manual at the same time
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-r", "--random", action="store_true", help="Pick a random ASCII file automatically")
    group.add_argument("-m", "--manual", action="store_true", help="Open the list to type a file name")
    args = parser.parse_args()

    # Using Path.home() makes this portable across different users and OSs
    home_dir = Path.home()
    source_folder = home_dir / ".config/fastfetch/ASCII Collection"
    destination_file = home_dir / ".config/fastfetch/ascii.txt"

    if not source_folder.exists():
        print(f"Error: Folder not found at {source_folder}")
        return

    # Grab only valid files
    files = [f for f in source_folder.iterdir() if f.is_file()]

    if not files:
        print("No files found in collection.")
        return

    # Logic based on CMD arguments
    selected_file = None

    if args.random:
        selected_file = random.choice(files)
        print(f"CMD Random Mode: Selected '{selected_file.name}'")
    elif args.manual:
        selected_file = get_user_choice(files)
    else:
        # Default behavior if no arguments are passed
        print("\n--- Fastfetch ASCII Selector ---")
        print("1. Random")
        print("2. Manual (Type exact name)")
        mode = input("Choice: ").strip()
        
        if mode == "1":
            selected_file = random.choice(files)
            print(f"Randomly selected: '{selected_file.name}'")
        elif mode == "2":
            selected_file = get_user_choice(files)
        else:
            print("Invalid choice. Exiting.")
            return

    # Copy the selected file
    try:
        shutil.copyfile(selected_file, destination_file)
        print(f"Successfully applied '{selected_file.name}' to Fastfetch.")
    except Exception as e:
        print(f"Error applying file: {e}")

if __name__ == "__main__":
    main()
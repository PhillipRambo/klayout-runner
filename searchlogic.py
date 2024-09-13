import os
from pick import pick


def list_gds_files():
    """
    Lists .gds files in the current directory and its subdirectories.

    Returns:
        tuple: (full_paths, file_names, current_dir_name, relative_paths)
            - full_paths: List of full paths to .gds files in the current directory and subdirectories.
            - file_names: List of .gds file names found in the directory and subdirectories.
            - current_dir_name: Name of the current working directory.
            - relative_paths: List of paths to .gds files relative to the current directory.
    """
    current_directory = os.getcwd()
    full_paths = []
    file_names = []
    relative_paths = []
    file_names_curr = []

  # Gather .gds files from the current directory
    for file_name in os.listdir(current_directory):
        if file_name.endswith('.gds'):
            file_names_curr.append(file_name)  
    for root, _, files in os.walk(current_directory):
        for file_name in files:
            if file_name.endswith('.gds'):
                full_path = os.path.join(root, file_name)
                full_paths.append(full_path)
                file_names.append(file_name)
                relative_path = os.path.relpath(full_path, current_directory)
                

                path_components = relative_path.split(os.sep)
                if len(path_components) > 2:
                    relative_path = os.path.join(path_components[-3], path_components[-2], path_components[-1])
                
                relative_paths.append(relative_path)
    current_dir_name = os.path.basename(current_directory)
    return full_paths, file_names, current_dir_name, relative_paths, file_names_curr


if __name__ == "__main__":
    full_paths, file_names, current_dir_name, relative_paths, file_names_curr = list_gds_files()
    print(f"Full Paths: {full_paths}")
    print(f"File Names: {file_names}")
    print(f"Current Directory Name: {current_dir_name}")
    print(f"Relative Paths: {relative_paths}")
    print(f"File Names Current: {file_names_curr}")



def select(folder_name):
    print("1. Search Current dir: " + '(' + folder_name + ')')
    print("2. Search Current dir: " + '(' +folder_name +')'+ " with children")
    choice = input("Enter 1 or 2: ")
    if choice == '1':
        return 'notchildren'
    elif choice == '2':
        return 'children'
    else:
        print("Invalid choice. Defaulting to Current dir" + folder_name)
        return 'notchildren'


def selection_menu_notchildren(file_names, full_paths):
    title = 'Select Layout'
    _, index = pick(file_names, title, indicator='=>', default_index=0)
    final_path = full_paths[index]
    return final_path



def selection_menu_children(relative_paths, full_paths):
    display_menu = [f.replace(os.sep, ' | ') for f in relative_paths]
    title = 'Select Layout'
    _, index = pick(display_menu, title, indicator='=>', default_index=0)
    final_path = full_paths[index]
    return final_path
    




def main():
    full_paths, file_names, current_dir_name, relative_paths, file_names_curr = list_gds_files()
    decision = select(current_dir_name)
    if decision == 'children':
        if not file_names:
            print("No. gds files found in the current directory.")
            return
        full_path = selection_menu_children(relative_paths, full_paths)
        print('Full Path: ' + full_path)
    else:
        if not file_names:
            print("No .gds files found in the current directory.")
            return
        full_path = selection_menu_notchildren(file_names_curr, relative_paths)
        print('Full Path: ' + full_path)

if __name__ == "__main__":
    main()


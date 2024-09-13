#!/usr/bin/env python3 
import subprocess
import os
from pick import pick
from searchlogic import select, selection_menu_children, selection_menu_notchildren, list_gds_files
import sys


current_dir = os.path.dirname(os.path.abspath(__file__))
rubyfile_dark = os.path.join(current_dir, 'ColorPalette_dark.rb')
rubyfile_light = os.path.join(current_dir, 'ColorPalette_light.rb')

print(rubyfile_dark)


def prompt_mode():
    print("Choose the mode to open KLayout:")
    print("1. Dark mode")
    print("2. Light mode")
    print("Enter 1 or 2, b:Back, e:Exit:: ", end="")
    choice = input().strip().lower()
    if choice == '1':
        return 'dark_mode'
    elif choice == '2':
        return 'light_mode'
    elif choice == 'b':
        return 'back'
    elif choice == 'e':
        print('Bye ...')
        sys.exit()
    else:
        print("Invalid choice. Defaulting to Light mode.")
        return 'light_mode'

def prompt_open_file():
    print("Do you wish to open a GDS file? Y/N, b:Back, e:Exit: ", end="")
    choice = input().strip().lower()
    if choice == 'y':
        return 'open'
    elif choice == 'n':
        return 'skip'
    elif choice == 'b':
        return 'back'
    elif choice == 'e':
        print('Bye ...')
        sys.exit()
    else:
        print("Invalid choice. Defaulting to skip.")
        return 'skip'


def direc_choice():
    print("Choose GDS Passing:")
    print("1. Search Current Directory")
    print("2. Type Directory")
    print("Select 1 or 2, b (Back), e Exit): ", end="")
    choice = input().strip().lower()
    if choice == '1':
        return 'search_curr_dir'
    elif choice == '2':
        return 'type_dir'
    elif choice == 'b':
        return 'back'
    elif choice == 'e':
        print('Bye ...')
        sys.exit()
    else:
        print("Invalid choice. Defaulting to search current dir.")
        return 'search_curr_dir'

def prompt_file_path():
    print("Enter the path to the GDS file, b (Back), e (Exit): ", end="")
    return input().strip()

def open_klayout(command):
    print(f"Running command: {command}")
    subprocess.run(command, shell=True)

def main():
    state = 'initial'
    command = None
    while True:
        if state == 'initial':
            mode = prompt_mode()
            if mode == 'back':
                print("No previous state to go back to.")
                continue
            state = 'choose_file'
            if mode == 'dark_mode':
                command = 'klayout -e -rm ' + rubyfile_dark
            else:
                command = 'klayout -e -rm ' + rubyfile_light

        elif state == 'choose_file':
            choice = prompt_open_file()
            if choice == 'back':
                state = 'initial'
                continue
            elif choice == 'open':
                state = 'search_or_type'
            elif choice == 'skip':
                command += ' &'
                open_klayout(command)
                break

        elif state == 'search_or_type':
            search = direc_choice()
            if search == 'back':
                state = 'choose_file'
                continue
            elif search == 'search_curr_dir':
                full_paths, file_names, current_dir_name, relative_paths, file_names_curr = list_gds_files()
                decision = select(current_dir_name)
                if decision == 'children':
                    if not file_names:
                        print("No .gds files found in the current directory.")
                        state = 'choose_file'
                        continue
                    full_path = selection_menu_children(relative_paths, full_paths)
                    command += f' {full_path}'
                elif decision == 'notchildren':
                    if not file_names_curr:
                        print("No .gds files found in the current directory.")
                        state = 'choose_file'
                        continue
                    full_path = selection_menu_notchildren(file_names_curr, relative_paths)
                    command += f' {full_path}'
            elif search == 'type_dir':
                full_path = prompt_file_path()
                if full_path == 'b':
                    state = 'choose_file'
                    continue
                command += f' {full_path}'
            
            command += ' &'
            open_klayout(command)
            break

if __name__ == "__main__":
    main()



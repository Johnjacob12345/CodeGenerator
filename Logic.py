import os
import shutil
import sys



def print_logic_info(shooterTabs=None, projectName=None):
    print("Logic.py is running")
    # Read and modify the file

    home_dir = os.path.expanduser("~")  # Get the user's home directory
    destination_directory = os.path.join(home_dir, "Documents")


    source_directory = "shellTest"

   
    # Copy entire directory tree
    shutil.copytree(source_directory, destination_directory, dirs_exist_ok=True)
    print(f"Copied entire directory from {source_directory} to {destination_directory}")
    print(f"{projectName}")

    os.rename(f"{destination_directory}\\ProjectName", f"{destination_directory}\\{projectName}")
    
    # with open(f"{destination_directory}\\{projectName}\\fileTest.txt", "r") as file:
    #     content = file.readlines()


    # content.insert(0, "//It works!\n")
# Write back the modified content
    # with open(f"{destination_directory}\\{projectName}\\fileTest.txt", "w") as file:
    #     file.writelines(content)

    print("Java file updated successfully!")
    
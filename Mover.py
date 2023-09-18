import os
from os.path import join, splitext
from PIL import Image
import shutil
import configparser

def process_files(root_folder, output_folder):
    """
    Process image files in the root_folder, read their aesthetic scores from the PNG info,
    and sort them into separate folders based on their aesthetic scores.
    :param root_folder: The folder containing the image files to process.
    :param output_folder: The folder where the sorted image files will be stored.
    """
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Iterate through each file in the root folder
    for entry in os.scandir(root_folder):
        if entry.name in {'aesthetic', 'not_aesthetic'} or entry.is_dir():
            continue
        
        file_path = entry.path
        _, file_extension = splitext(file_path)
        if file_extension.lower() != '.png':
            continue
        
        try:
            with Image.open(file_path) as img:
                # Get the aesthetic score from the PNG info
                aesthetic_score = float(img.info.get("aesthetic_score", 0.0))
            
            # Determine the target folder based on the aesthetic score
            score_folder = "aesthetic" if aesthetic_score >= 7.0 else "not_aesthetic"
            # Create a decimal folder name based on the aesthetic score
            decimal_folder = "{:.1f}".format(aesthetic_score)
            target_folder = os.path.join(output_folder, score_folder, decimal_folder)
            
            if not os.path.exists(target_folder):
                os.makedirs(target_folder)
            
            # Copy the file to the target folder
            try:
                shutil.copy2(file_path, os.path.join(target_folder, entry.name))
                print(f"Moved {entry.name} to {target_folder}")
                os.remove(file_path)  # Delete the original file
            except PermissionError as e:
                print(f"Error moving file {file_path}: {e}")
        except PermissionError as e:
            print(f"Error processing file {file_path}: {e}")

# Read the config.ini file
config = configparser.ConfigParser()
config.read('config.ini')

# Get the root_folder and output_folder from the config.ini file
root_folder = config.get('Paths', 'root_folder')
output_folder = config.get('Paths', 'output_folder')

# Process the root_folder
process_files(root_folder, output_folder)
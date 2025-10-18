import os, shutil, json, logging

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # folder of the script
config_path = os.path.join(BASE_DIR, 'config.json')

try:
    with open(config_path, 'r') as f:
        config = json.load(f)
        target_directory = config['Target_Directory']
        destination_directory = config['Destination_Directories']
        file_types = config['File_Types']

except FileNotFoundError:
    logging.error(f"Configuration file not found at: {config_path}")

except Exception as e:
    logging.error(f"An error occurred while loading the configuration: {e}")

logging.basicConfig(filename='file_sorter.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def file_check(target_directory, destination_directory):
    """
    Checks if target and destination directories exist.
    Creates missing destination folders automatically.
    Logs all actions and errors.
    """
    try:
        if not os.path.exists(target_directory):
            logging.error(f"Target directory '{target_directory}' does not exist.")
        else:
            logging.info(f"Target directory '{target_directory}' found.")

        for file_name, dest in destination_directory.items():
            if not os.path.exists(dest):
                logging.error(f"Destination directory: '{file_name}' does not exist.")
                os.makedirs(dest, exist_ok=True)
                logging.info(f"Created destination directory :'{file_name}'.")
            else:
                logging.info(f"Destination directory: '{file_name}' found.")
    except Exception as e:
        logging.error(f"An error occurred during file check: {e}")


def scan_and_move_files(target_directory):
    """
    Scans all files in the target directory and sorts them into destination folders
    based on their extensions defined in the config. 
    - Moves matched files to their category folder.
    - Renames duplicates by appending "_1".
    - Moves unmatched files to the 'Others' folder if specified.
    - Logs all actions and errors.
    """
    try:
        for files in os.listdir(target_directory):
            file_name = files.split('.')[0]
            extention = os.path.splitext(files)[1]
            if not extention:
                continue

            for category,ext_list in file_types.items():
                moved=False
                if category=='Others':
                    shutil.move(os.path.join(target_directory, files), destination_directory.get('Others'))
                    break
                for extentions in ext_list:
                    if extention == extentions:
                        dest_dir = destination_directory.get(category)
                        if dest_dir :
                            if not os.path.exists(os.path.join(dest_dir, files)):
                                shutil.move(os.path.join(target_directory, files), dest_dir)
                                moved = True
                                logging.info(f"Moved file '{files}' to '{dest_dir}'.")
                                break
                            else:
                                new_file=file_name+"_1"+extention
                                os.rename(os.path.join(target_directory, files), os.path.join(dest_dir, new_file))
                                moved = True
                                logging.info(f"Renamed and moved duplicate file '{files}' to '{new_file}' in '{dest_dir}'.")
                                break
                if moved:
                    break

    except Exception as e:
        logging.error(f"An error occurred while scanning files: {e}")


if __name__ == "__main__":
    file_check(target_directory, destination_directory)
    scan_and_move_files(target_directory)
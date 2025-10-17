import logging
import os
import shutil
import json
import requests
from datetime import datetime
from colorama import Fore, Style

# Load configuration
try:
    with open("config.json","r") as file:
            config=json.load(file)
except Exception as e:
    print(f"Error loading config: {e}")

# Setup logging
logging.basicConfig(
    filename=config['log_file'] if 'log_file' in config else 'warmup.log',
    level=logging.INFO,
    format="%(asctime)s-%(levelname)s-%(message)s"
)

logging.info("Warmup script started.")


#file handling
def file_handling():
    try:
        with open("motivated.txt","w") as file:
            file.write("I will not stop until i win...\nThe world will witness a greatness in future")

        with open("motivated.txt","r") as file:
            content=file.read()
            print("file content: ",content)

        logging.info("File handling done successfully")
        print(Fore.GREEN + "File handled successfully!" + Style.RESET_ALL)
        return True

    except Exception as e:
        logging.error(f"Error in file handling: {e}")
        return False

# file organize 
def file_organization():
    try:
        os.makedirs(config["folders"]["output"], exist_ok=True)

        with open("warmup_file.txt","w") as file:
            file.write("This is a warmup file")
        
        shutil.move("warmup_file.txt",config["folders"]["output"])

        logging.info("File organized successfully")
        print(Fore.GREEN + "File moved successfully!" + Style.RESET_ALL)
        return True

    except Exception as e:
        logging.error(f"Error in file organization: {e}")
        return False

# API call
def api_call():
    try:
        response=requests.get(config["api_url"])
        data=response.json()
        print("Github Name:",data["name"])
        print("Public Repos:",data["public_repos"])

        logging.info("API data fetched successfully")
        print(Fore.GREEN + "API call successful!" + Style.RESET_ALL)
        return True
    
    except Exception as e:
        logging.error(f"Error in API call: {e}")
        return False

#OOP 
def oop_section():
    try:
        class Developer:
            def __init__(self, name, language):
                self.name = name
                self.language = language
                self.joined=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            def code(self):
                return f"{self.name} is coding in {self.language} | Joined on {self.joined}"
        dev = Developer("Karnan","Python")
        print(dev.code())

        logging.info("OOP section executed successfully")
        print(Fore.GREEN + "OOP executed successfully!" + Style.RESET_ALL)
        return True

    except Exception as e:
        logging.error(f"Error in OOP section: {e}")
        return False

logging.info("Warmup script ended.")

# task completed details
if __name__ == "__main__":
    
    tasks_done={
        "file_handling":file_handling(),
        "file_organization":file_organization(),
        "api_call":api_call(),
        "oop_section":oop_section()
    }

    print("\nTask Completion Summary:")
    task_completed=0
    for task, status in tasks_done.items():
        if status:
           task_completed+=1
    print(f"Total Tasks Completed: {Fore.GREEN+str(task_completed)+Style.RESET_ALL} out of {len(tasks_done)}")
    print(f"Total Tasks Failed: {Fore.RED+str(len(tasks_done)-task_completed)+Style.RESET_ALL} out of {len(tasks_done)}")
    
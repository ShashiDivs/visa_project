import os
from pathlib import Path
import logging


while True:
    project_name = input("Enter your Project Name : ")
    if project_name !="":
        break

logging.info("Creating project by Name")

list_of_files = [

    ".github/workflows/.gitignore",
    ".github/workflows/main.yaml",
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/config/__init__.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/utils/__init__.py",
    f"config/config.yaml",
    "requirements.txt",
    "setup.py",
    "main.py",
    "schema.yaml"

]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,file_name = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info("Cretaing a New Directory at : {file_dir} for file: {file_name}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"Creating a new file: {file_name} for path {filepath}")

    else:
        logging.info(f"file is already present at : {filepath}")

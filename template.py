import os
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: - %(levelname)s:- - %(message)s')

list_of_files = [
    "README.md",
    "requirements.txt",
    ".env",
    ".gitignore",
    "setup.py",
    "app.py",
    "src/__init__.py",
    #"src/data/__init__.py",
    #"src/tools/__init__.py",
    #"src/client/__init__.py",
    #"src/config/__init__.py",
    #"src/modules/__init__.py",
    #"src/utils/__init__.py"
    "src/utils/helper.py",
    "src/utils/prompt.py",
    #"src/notebooks/__init__.py",
    "src/notebooks/EDA.ipynb",
    #"src/tests/__init__.py",
    #"src/tests/test_helper.py",
    ]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir}")

    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"File already exists: {filepath}")
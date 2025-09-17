import os
import shutil
import argparse

from pathlib import Path
from modules.logger import logging


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--project_name", required=True, type=str, help="The Name of the project you wish to create its structure"
    )
    return parser


def create_project_structure(project_name):
    list_of_files = [
        f"{project_name}/.github/workflows/.gitkeep",
        f"{project_name}/src/__init__.py",
        f"{project_name}/src//components/__init__.py",
        f"{project_name}/src/utils/__init__.py",
        f"{project_name}/src/config/configurations.py",
        f"{project_name}/src/config/__init__.py",
        f"{project_name}/src/pipeline/__init__.py",
        f"{project_name}/src/entity/__init__.py",
        f"{project_name}/src/constants/__init__.py",
        f"{project_name}/EDA/trials.ipynb",
        f"{project_name}/config/config.yaml",
        f"{project_name}/dvc.yaml",
        f"{project_name}/params.yaml",
        f"{project_name}/requirements.txt",
        f"{project_name}/setup.py",
        f"{project_name}/README.md",
        f"{project_name}/exception/__init__.py",
        f"{project_name}/exception/_exception.py",
        f"{project_name}/logger/__init__.py",
        f"{project_name}/logger/_logger.py",
    ]

    for file_path in list_of_files:
        file_path = Path(file_path)
        file_dir, file_name = os.path.split(file_path)
        if file_dir != "":
            os.makedirs(file_dir, exist_ok=True)
            logging.info(f"Creating directory: {file_dir} for the file: {file_name}")
        if (not os.path.exists(file_path)) or (os.path.getsize(file_path) != 0):
            with open(file_path, "w") as file:
                pass
                logging.info(f"Creating empty file: {file_name}")
        else:
            logging.info(f"the file {file_name} already exists")

    files_to_copy = [
        f"modules/exception/__init__.py",
        f"modules/exception/_exception.py",
        f"modules/logger/__init__.py",
        f"modules/logger/_logger.py",
    ]

    for file_name in files_to_copy:
        new_file_name = os.path.join(str(project_name), file_name.replace("modules/", ""))
        logging.info(f"Coping the file form: {file_name} to {new_file_name}")

        logging.info(f"Coping the file form: {file_name} to {new_file_name}")
        shutil.copy2(file_name, new_file_name, follow_symlinks=True)


if __name__ == "__main__":
    parse = get_parser()
    params = parse.parse_args()
    project_name = params.project_name
    create_project_structure(project_name)

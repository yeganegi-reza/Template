import os
import sys
import shutil
import argparse

from pathlib import Path
from reytools.logger import logging
from reytools.exception import CustomException


import subprocess


def create_project_dir(project_name):
    if os.path.exists(project_name):
        try:
            raise ValueError("The Project Directory Exists, Remove it or change the Project Dir")
        except Exception as e:
            raise CustomException(e, sys)

    else:
        os.makedirs(project_name, exist_ok=True)
        logging.info("The project dir created")
        project_dir = os.path.join(os.getcwd(), f"{project_name}", "")
        return project_dir


def init_repo(project_dir):
    subprocess.check_call(["git", "init"], cwd=project_dir)
    logging.info(f"Initialized empty Git repository in {project_dir}")


def add_files_to_git(project_dir):
    subprocess.check_call(["git", "add", "."], cwd=project_dir)
    logging.info(f"All files in {project_dir} was added to the git repo")


def add_reytools_to_project(project_dir):
    src_dir = os.path.join(project_dir, "src", "")
    sub_module_link = "https://github.com/yeganegi-reza/reytools.git"
    subprocess.check_call(["git", "submodule", "add", sub_module_link], cwd=src_dir)

def add_reylearn_to_project(project_dir):
    src_dir = os.path.join(project_dir, "src", "")
    sub_module_link = "https://github.com/yeganegi-reza/reylearn.git"
    subprocess.check_call(["git", "submodule", "add", sub_module_link], cwd=src_dir)


def first_commit(project_dir):
    subprocess.call(["git", "commit", "-m", "The Project Structure created"], cwd=project_dir)
    logging.info(f"Project first commit in {project_dir}")


def first_push(project_dir, repo_url):
    subprocess.check_call(["git", "branch", "-M", "main"], cwd=project_dir)
    subprocess.check_call(["git", "remote", "add", "origin", repo_url], cwd=project_dir)
    subprocess.check_call(["git", "push", "-u", "origin", "main"], cwd=project_dir)


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--project_name", required=True, type=str, help="The Name of the project you wish to create its structure"
    )
    parser.add_argument(
        "--repo_url", required=True, type=str, help="The git URL of the the project, repo should be empty"
    )

    return parser


def create_project_structure(project_name):
    list_of_files = [
        f"{project_name}/.github/workflows/main.yaml",
        f"{project_name}/src/__init__.py",
        f"{project_name}/src//components/__init__.py",
        f"{project_name}/src/config/configurations.py",
        f"{project_name}/src/config/__init__.py",
        f"{project_name}/src/pipeline/__init__.py",
        f"{project_name}/src/tools/__init__.py",
        f"{project_name}/EDA/trials.ipynb",
        f"{project_name}/config/project_config.yaml",
        f"{project_name}/dvc.yaml",
        f"{project_name}/requirements.txt",
        f"{project_name}/README.md",
        f"{project_name}/setup.py",
        f"{project_name}/Dockerfile",
        f"{project_name}/templates/index.html",
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


def copy_comp_creators_files(project_dir):
    files_to_copy = ["comp.txt", "pipeline.txt", "create_comp_pipeline.py"]
    for file_name in files_to_copy:
        file_path = Path(os.path.join("template_files", file_name))
        new_file_name = Path(project_dir)
        logging.info(f"Coping the file from: {file_path} to {new_file_name}")
        shutil.copy2(file_path, new_file_name, follow_symlinks=True)


def copy_config_class_files(project_dir):
    files_to_copy = ["configurations.py", "__init__.py"]
    for file_name in files_to_copy:
        file_path = Path(os.path.join("template_files", "config", file_name))
        new_file_name = Path(project_dir, "src", "config")
        logging.info(f"Coping the file from: {file_path} to {new_file_name}")
        shutil.copy2(file_path, new_file_name, follow_symlinks=True)


def copy_git_ignore(project_dir):
    file_name = ".gitignore"
    new_file_name = os.path.join(project_dir, ".gitignore")
    logging.info(f"Coping the file from: {file_name} to {new_file_name}")
    shutil.copy2(file_name, new_file_name, follow_symlinks=True)

def copy_dockerfile(project_dir):
    file_name = "DockerFile"
    new_file_name = os.path.join(project_dir, "DockerFile")
    logging.info(f"Coping the file from: {file_name} to {new_file_name}")
    shutil.copy2(file_name, new_file_name, follow_symlinks=True)

if __name__ == "__main__":
    parse = get_parser()
    params = parse.parse_args()
    project_name = params.project_name
    repo_url = params.repo_url
    project_dir = create_project_dir(project_name=project_name)
    try:
        create_project_structure(project_name)
        copy_comp_creators_files(project_dir=project_name)
        copy_git_ignore(project_dir)
        copy_dockerfile(project_dir)
        copy_config_class_files(project_dir)
        init_repo(project_dir=project_dir)
        add_reytools_to_project(project_dir)
        add_reylearn_to_project(project_dir) 
        add_files_to_git(project_dir=project_dir)
        first_commit(project_dir=project_dir)
        first_push(project_dir=project_dir, repo_url=repo_url)
    except Exception as e:
        if os.path.exists(project_dir):
            shutil.rmtree(project_dir)
        logging.info("Project Creation Failed")
        raise CustomException(e, sys)

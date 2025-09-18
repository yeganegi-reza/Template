from pathlib import Path
import os


def create_comp(comp_name, comp_file_path):
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = Path(os.path.join(cur_dir, "comp.txt"))
    with open(file_path, "r") as file:
        all_file_content = file.read()

    all_file_content = all_file_content.replace("{comp_name}", comp_name)
    with open(comp_file_path, "w") as file:
        file.write(all_file_content)


def create_pipeline(comp_name, pipleline_file_path):
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = Path(os.path.join(cur_dir, "pipeline.txt"))
    with open(file_path, "r") as file:
        all_file_content = file.read()

    all_file_content = all_file_content.replace("{comp_name}", comp_name)
    with open(pipleline_file_path, "w") as file:
        file.write(all_file_content)


def create_comp_dir(comp_dir):
    os.makedirs(comp_dir, exist_ok=True)


def check_comp_name(comp_name: str):
    splits = comp_name.split(" ")
    assert len(splits) == 2
    cap_splits = [s.capitalize() for s in splits]
    file_name = splits[0] + "_" + splits[1]
    class_name = cap_splits[0] + cap_splits[1]
    return file_name, class_name


cur_dir = os.path.dirname(os.path.abspath(__file__))
comp_name = "test comp"

file_name, class_name = check_comp_name(comp_name=comp_name)
comp_dir = Path(os.path.join(cur_dir, "src", "components", file_name))
comp_file_path = Path(os.path.join(comp_dir, f"_{file_name}.py"))
pipeline_file_path = Path(os.path.join(cur_dir, "src", "pipeline", f"stage_{file_name}.py"))
create_comp_dir(comp_dir)
create_comp(class_name, comp_file_path)
create_pipeline(class_name, pipeline_file_path)

from pathlib import Path 

working_directory = Path(__file__).parents[1]

paths_directory = {
    "users":  working_directory / "datalake/users",
    "data_warehouse": working_directory / "data_warehouse",
    "avatars": working_directory / "data_warehouse/avatars"
}

def setup_folder_structure():
    for path in paths_directory.values():
        path.mkdir(parents=True, exist_ok=True)



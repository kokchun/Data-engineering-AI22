from setup import setup_folder_structure, paths_directory
from extract_data import extract_users
from transform import Transforms
from load import Load


if __name__ == "__main__":

    setup_folder_structure()
    extract_users(10, paths_directory["users"])

    avatar_df = Transforms(paths_directory["users"]).avatar_df()

    ids, urls = avatar_df["id"], avatar_df["avatar"]

    print(urls, ids)
    loader = Load(paths_directory["data_warehouse"])

    map_df = Transforms(paths_directory["users"]).map_dashboard_df

    loader.load_avatars(urls, ids)
    loader.load_csv_dashboard(map_df)
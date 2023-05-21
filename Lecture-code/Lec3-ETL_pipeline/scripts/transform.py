#%%
import json
import pandas as pd 


class _DatalakeProvider:
    """Provides raw data in an easy interface"""
    def __init__(self, users_directory) -> None:
        self.all_users = []
        for filepath in users_directory.iterdir():
            with open(filepath, 'r') as file:
                user_data = json.load(file)
            self.all_users.append(user_data)
            
    @property
    def raw_df(self):
        return pd.DataFrame(self.all_users)

#%%    
class Transforms:
    """Different transforms for different downstreams use cases"""
    def __init__(self, users_directory):
        columns_keep = ["id", "first_name", "last_name", "username", "email", "phone_number", "address", "date_of_birth", "avatar"]

        self.base_df = _DatalakeProvider(users_directory).raw_df[columns_keep]
    
    @property
    def map_dashboard_df(self):
        df = self.base_df[["id", "first_name", "last_name", "date_of_birth"]]
        cities = self.base_df["address"].apply(lambda row: row["city"])
        coordinates = self.base_df["address"].apply(lambda row: row["coordinates"])

        longitudes = coordinates.apply(lambda row: row["lng"])
        latitudes = coordinates.apply(lambda row: row["lat"])

        for name, column in zip(["city", "latitude", "longitude"],[cities, latitudes, longitudes]):
            df.insert(loc = df.shape[1], column = name, value = column)

        full_name =  df["first_name"] + " " + df["last_name"]
        df.insert(2, "name", full_name)

        df = df.drop(columns = ["first_name", "last_name"])

        return df


    def avatar_df(self):
        return self.base_df[["id","avatar"]]
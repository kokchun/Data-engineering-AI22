import time, requests

class Load:
    def __init__(self, data_warehouse_path) -> None:
        self.avatar_path = data_warehouse_path / "avatars"
        self.data_warehouse_path = data_warehouse_path

    def load_avatars(self, urls, ids):
        
        for avatar_url, id in zip(urls, ids):
            response = requests.get(avatar_url)

            with open(self.avatar_path / f"{id}.png" , "wb") as file:
                file.write(response.content)

            time.sleep(2)
    
    def load_csv_dashboard(self, df):
        df.to_csv(self.data_warehouse_path/"users.csv")

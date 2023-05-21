# %%
import requests, json, time

def extract_users(number_users: int, users_directory: str):
    for _ in range(number_users):
        data = requests.get("https://random-data-api.com/api/v2/users").json()

        with open(users_directory / f"{data['id']}.json", "w") as file:
            json.dump(data, file)

        print(f"Extracting user with id {data['id']}")
        time.sleep(2)

if __name__ == "__main__":
    extract_users(10)

# %%

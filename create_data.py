import requests

BASE_URL = "http://localhost:8000"

def create_users(count: int):
    url = f"{BASE_URL}/create_users/{count}"
    response = requests.post(url)
    if response.status_code == 200:
        print(f"{count} fake users created successfully")
    else:
        print(f"Failed to create fake users, status code: {response.status_code}")
def create_products(count: int):
    url = f"{BASE_URL}/create_products/{count}"
    response = requests.post(url)
    if response.status_code == 200:
        print(f"{count} fake users created successfully")
    else:
        print(f"Failed to create fake users, status code: {response.status_code}")
def create_orders(count: int):
    url = f"{BASE_URL}/create_orders/{count}"
    response = requests.post(url)
    if response.status_code == 200:
        print(f"{count} fake users created successfully")
    else:
        print(f"Failed to create fake users, status code: {response.status_code}")
if __name__ == "__main__":
    create_users(10) 
    create_products(14)
    create_orders(2)
import requests

def fetch_random_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()
    # print(data)
    
    if data["success"] and "data" in data:
        userdata = data["data"]
        username = userdata["login"]["username"]
        print(username)
        country = userdata["location"]["country"]
        print(country)
    else:
        raise Exception("Failed to fetch userdata!!!")

def main():
    try:
        fetch_random_user()
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()
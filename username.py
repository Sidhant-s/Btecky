import requests

def get_github_user_info(username):
    api_url = f"https://api.github.com/users/{username}"
    response = requests.get(api_url)

    if response.status_code == 200:
        user_data = response.json()
        print(f"GitHub User Information for {username}:")
        print(f"Name: {user_data['name']}")
        print(f"Bio: {user_data['bio']}")
        print(f"Followers: {user_data['followers']}")
        print(f"Following: {user_data['following']}")
    else:
        print(f"Failed to fetch information for user {username}. Status Code: {response.status_code}")

# Input a GitHub username to fetch information
github_username = input("Enter a GitHub username: ")
get_github_user_info(github_username)

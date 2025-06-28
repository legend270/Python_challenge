 #Day 14 of the 90 days python challenge
  #  Go to GitHub → Settings → Developer settings → Personal access tokens

   # Generate a new token with "read:user" scope

    #Save this token securely (treat it like a password)












import requests

# Configuration
GITHUB_API = "https://api.github.com"
TOKEN = "your_personal_access_token_here"  # Replace with your token
USERNAME = "octocat"  # Default to GitHub's mascot

# Set up headers with authentication
headers = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def get_user_profile(username):
    """Fetch GitHub user profile information"""
    url = f"{GITHUB_API}/users/{username}"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

# Get user input
username = input("Enter GitHub username (or press Enter for default): ") or USERNAME

# Fetch and display profile
profile = get_user_profile(username)
if profile:
    print("\nGitHub Profile Information:")
    print(f"Username: {profile['login']}")
    print(f"Name: {profile.get('name', 'Not specified')}")
    print(f"Bio: {profile.get('bio', 'Not specified')}")
    print(f"Public Repos: {profile['public_repos']}")
    print(f"Followers: {profile['followers']}")
    print(f"Following: {profile['following']}")
    print(f"Profile URL: {profile['html_url']}")
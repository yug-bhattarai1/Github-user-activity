import requests


def get_github_events(username):
    url = f'https://api.github.com/users/{username}/events'

    # headers = {'User-Agent': 'Mozilla/5.0'} "Just use when github doesn't respond (403 error), otherwise not needed"
    
    r = requests.get(url, timeout = 5) #add (headers=headers) if needed
    
    if r.status_code == 200:
        events = r.json()
        
        for event in events[:10]:  
            print(f"Type: {event['type']} | Repo: {event['repo']['name']}")
    else:
        print(f"Failed to fetch events. Status code: {r.status_code}")


username = input("Enter a GitHub username: ")
get_github_events(username)




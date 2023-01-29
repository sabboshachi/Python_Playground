pip install requests
import requests

username = 'instagram_username'
url = f'https://www.instagram.com/{username}/?__a=1'
response = requests.get(url)
data = response.json()
profile_pic_url = data['graphql']['user']['profile_pic_url_hd']
response = requests.get(profile_pic_url)
open(f'{username}.jpg', 'wb').write(response.content)

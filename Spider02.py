import requests

# 注意：请替换为你的实际Cookie
headers = {
    'cookie': "请替换为你的Cookie",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    'referer': "https://music.163.com/",
}

# 注意：params 和 encSecKey 需要根据实际请求获取
url = 'https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token=your_csrf_token'

data = {
    "params": "your_params",
    "encSecKey": "your_encSecKey"
}

response = requests.post(url, data=data, headers=headers)
json_data = response.json()

music_url = json_data['data'][0]['url']

music_content = requests.get(url=music_url, headers=headers).content

with open('music\\downloaded.mp3', 'wb') as f:
    f.write(music_content)

print(music_url)

import requests
import execjs
from config import *

# 注意：请替换为你的实际Cookie
headers = {
    'cookie': "请替换为你的Cookie",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    'referer': "https://music.163.com/",
}

if choice == 1:
    music_url = f'https://music.163.com/song/media/outer/url?id={music_id}.mp3'
    print("=========使用链接下载=========")
elif choice == 2:
    js_code = execjs.compile(open('wyy.js', encoding='utf-8').read())
    i6c = {
        "ids": f"[{music_id}]",
        "level": "exhigh",
        "encodeType": "aac",
        "csrf_token": "your_csrf_token"
    }
    r = js_code.call('GetSign', i6c)
    url = 'https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token=your_csrf_token'
    data = {
        "params": r['encText'],
        "encSecKey": r['encSecKey'],
    }

    response = requests.post(url, data=data, headers=headers)
    json_data = response.json()
    music_url = json_data['data'][0]['url']
    print('=========使用逆向JS下载=========')

music_content = requests.get(url=music_url, headers=headers).content

with open(f'music\\{title}.mp3', 'wb') as f:
    f.write(music_content)
print("音频文件保存完毕！")

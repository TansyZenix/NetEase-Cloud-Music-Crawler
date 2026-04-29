import re
import execjs
import requests
from config import *

"""
批量爬取数据: 分析请求参数的变化规律（逆向）
1. 通过开发者工具定位加密位置
2. 断点调试分析
"""

# 注意：请替换为你的实际Cookie
headers = {
    'cookie': "请替换为你的Cookie",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    'referer': "https://music.163.com/",
}

link = f'https://music.163.com/playlist?id={str(songListId)}'
html = requests.get(link, headers=headers).text
info = re.findall('<a href="/song\?id=(\d+)">(.*?)</a>', html)
i = 0

for music_id, title in info:
    i += 1
    if i > MAX_SONG_NUMS:
        break
    print(f'第{i}首歌，歌名为《{title}》，id={music_id}')

    js_code = execjs.compile(open('wyy.js', encoding='utf-8').read())
    i6c = {
        "ids": f"[{music_id}]",
        "level": "exhigh",
        "encodeType": "aac",
        "csrf_token": "your_csrf_token"
    }
    r = js_code.call('GetSign', i6c)
    print(r)

    url = 'https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token=your_csrf_token'

    data = {
        "params": r['encText'],
        "encSecKey": r['encSecKey'],
    }

    response = requests.post(url, data=data, headers=headers)
    json_data = response.json()
    music_url = json_data['data'][0]['url']

    music_content = requests.get(url=music_url, headers=headers).content

    with open(f'music\\{title}.mp3', 'wb') as f:
        f.write(music_content)

    print(music_url)

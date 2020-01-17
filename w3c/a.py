import json
import time

import requests


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}
# url = 'https://m.weibo.cn/api/container/getIndex?containerid=2304133176010690_-_WEIBO_SECOND_PROFILE_WEIBO&page_type=03&page=1'

url = 'https://m.weibo.cn/api/container/getIndex?uid=3176010690&luicode=10000011&lfid=100103type%3D1%26q%3D%E5%B8%A6%E5%B8%A6%E5%A4%A7%E5%B8%88%E5%85%84&type=uid&value=3176010690&containerid=1076033176010690&since_id={}'

first = 4457894177550242
while True:

    time.sleep(2)
    a = url.format(first)
    print(a)
    res = requests.get(a, headers=headers)
    res = json.loads(res.content.decode())

    since_id = res['data']['cardlistInfo']['since_id']
    print('since_id', since_id)
    first = since_id
    for i in res['data']['cards']:
        print(i['mblog']['text'])


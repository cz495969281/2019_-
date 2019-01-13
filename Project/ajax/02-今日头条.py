import requests
from urllib.parse import urlencode
from pprint import pprint


def get_page(offset):
    params = {
        "offset": offset,
        "format": "json",
        "keyword": "街拍",
        "autoload": "true",
        "count": "20",
        "cur_tab": "1",
        "from": "search_tab"

    }

    url = 'https://www.toutiao.com/search_content/?' + urlencode(params)

    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()

    except requests.ConnectionError:
        return None

# get_page()

def get_image(json):
    if json.get('data'):
        for item in json.get('data'):
            try:
                title = item.get('title')
                images = item.get('image_list')


                for image in images:
                    yield ({

                        'image': 'https:' + image.get('url'),
                        'title':title
                    })
            except Exception as e:
                pass


import os

from hashlib import md5

def save_image(item):
    if not os.path.exists(item.get('title')):
        os.mkdir(item.get('title'))

    try:
        response = requests.get(item.get('image'))
        if response.status_code == 200:
            file_path = '{0}/{1}.{2}'.format(item.get('title'),md5(response.content).hexdigest(),'jpg')
            if not os.path.exists(file_path):
                with open(file_path,'wb') as f:
                    f.write(response.content)
            else:
                print("已下载",file_path)

    except requests.ConnectionError:
        print("下载失败")

from multiprocessing.pool import Pool


def main(offset):
    json = get_page(offset)
    for item in get_image(json):
        print(item)
        save_image(item)


# main(1)
GROUP_START = 1
GROUP_END = 20

if __name__ == "__main__":

    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START,GROUP_END+1)])
    pool.map(main,groups)
    pool.close()
    pool.join()
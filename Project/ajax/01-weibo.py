import requests
from  urllib.parse import urlencode
from pprint import pprint
from pyquery import PyQuery as pq


# https://m.weibo.cn/u/5279716168?uid=5279716168&luicode=10000011&lfid=100103type%3D3%26q%3D%E9%99%88C%E6%B3%BDZ%26t%3D0
# https://m.weibo.cn/api/container/getIndex?type=uid&value=2830678474&containerid=1005052830678474
base_url = 'https://m.weibo.cn/api/container/getIndex?'
headers = {
    'Host': 'm.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/5279716168',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

def get_page(page):
    params = {
        'type': 'uid',
        'value': '5279716168',
        'containerid': '1076035279716168',
        'page': page
    }
    url = base_url + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json(), page
    except requests.ConnectionError as e:
        print('Error', e.args)


from pyquery import PyQuery as pq


def parse_page(json,page: int):
    if json:
        items = json.get('data').get('cards')
        for item in items:

            item = item.get('mblog')
            try:
                weibo = {}
                weibo['id'] = item.get('id')
                weibo['text'] = pq(item.get('text')).text()
                weibo['attitudes'] = item.get('attitudes_count')
                weibo['comments'] = item.get('comments_count')
                weibo['reposts'] = item.get('reposts_count')
                yield weibo
            except Exception as e:
                print("没有数据")


if __name__ == '__main__':
    for page in range(1, 11):
        json = get_page(page)
        results = parse_page(*json)
        for result in results:
            print(result)

        # print(results)
import json
from pprint import pprint

import jsonpath
import requests

url = 'http://www.lagou.com/lbs/getAllCitySearchLabels.json'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}

response = requests.get(url,headers=headers)

result = json.loads(response.text)

#使用jsonpath检索数据
search_result = jsonpath.jsonpath(result,"$..name")
pprint(search_result)

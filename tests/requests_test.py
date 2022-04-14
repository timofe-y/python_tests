# coding=utf-8

import json
import requests
from requests.auth import AuthBase

def printRequestedUrl(r, *args, **kwargs):
    print('printRequestedUrl')
#    print(r.url)
#    print(*args)
#    print(**kwargs)

def printData(r, *args, **kwargs):
    print('printData')
#    print(r.text)

def check_for_errors(r, *args, **kwargs):
    print('check_for_errors')
#   r.raise_for_status()


def test():
    url = 'https://digitology.tech/docs/requests/user/advanced.html#streaming-requests'
    # r = requests.get(url=url)
    # r.encoding = 'utf-8'
    # print(r.text)
    i = 0
    r = requests.get(url=url, stream=True)
    for line in r.iter_lines():
        s = line.decode('utf-8')
        print('{}) {}'.format(i,s))
        i = i + 1
    # r = requests.get('https://api.github.com/repos/psf/requests/issues/482')
    # issue = json.loads(r.text)
    # print(issue['title'])
    # print(issue['comments'])
    #
    # r = requests.get(r.url + '/comments')
    # comments = r.json()
    # print(comments[0].keys())
    # print(comments[2]['body'])
    # print(comments[2]['user']['login'])

    #getdata = requests.get('https://jsonplaceholder.typicode.com/users', hooks = {'response': [printRequestedUrl, printData,check_for_errors]})


    # r = requests.get('https://httpbin.org/stream/20', stream=True)
    # if r.status_code == requests.codes.ok:
    #     print(r.headers['content-type'])
    # for line in r.iter_lines():
    #
    #     # отфильтровать оставшиеся новые строки
    #     if line:
    #         decoded_line = line.decode('utf-8')
    #         print(json.loads(decoded_line))
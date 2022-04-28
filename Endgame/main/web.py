import requests
import re
from logger import *


log = logging.getLogger(':::::END_GAME:::::')

def get_method(url, auth, parameters, headers_dict):
    try:
        request = requests.get(url, auth=auth, timeout=5, params=parameters, headers=headers_dict)
        return request
    except Exception as err:
        return [err]


def post_method(url, auth, body, headers):
    try:
        request = requests.post(url=url, auth=auth, data=body, headers=headers)
        return request
    except Exception as er:
        return [er]


def put_method(url, auth, body, headers):
    try:
        request = requests.put(url=url, auth=auth, data=body, headers=headers)
        return request
    except Exception as err:
        return [err]


def patch_method(url, auth, body, headers):
    try:
        request = requests.patch(url=url, auth=auth, data=body, headers=headers)
        return request
    except Exception as err:
        return [err]


def delete_method(url):
    try:
        request = requests.delete(url)
        return request
    except Exception as err:
        return [err]


def web_surfer(args):

    output = {}
    method = args['method']
    url = args['endpoint']
    headers = args['headers']
    body = args['body']
    auth = args['auth']
    #auth_key = args['key_id']
    params = args['params']
    log_level = args['log']
    logger_start(log_level)
    log.info('Arguments parsed')
    methods = dict(GET=get_method(url, auth, params, headers), POST=post_method(url, auth, body, headers),
                   PUT=put_method(url, auth, body, headers), PATCH=patch_method(url, auth, body, headers),
                   DELETE=delete_method(url))
    valid_url = r'^(http|https)(://)\w+\S+$'
    if re.match(valid_url, url):
        log.info('URL valid. Trying connect to host')
        req = methods[method]
        if isinstance(req, list):
            output['Error'] = req[0]
            return output
            log.error('Connection ERROR!')
            log.debug('Please try another URL')
            #print(output)  # output
        else:
            log.info('Connection established')
            output['URL'] = req.url
            # req_status = (lambda x: 'OK' if x.ok else 'NOT FOUND' if x.status_code == 404 else "Something goes wrong")\
            # (req)
            # output['Response Status'] = req_status
            output['Response Status'] = req.reason
            output['Response Status Code'] = req.status_code
            log.info(f'RESPONSE CODE: {req.status_code} - STATUS: {req.reason}')
            # headers_select = (lambda y: request.headers[y] if y else request.headers)(headers_dict)
            output['headers'] = req.headers
            output['Response Time'] = round(req.elapsed.total_seconds(),2)
            return output
            log.info('DATA collected sucessfully')

    else:
        output['Error'] = 'Invalid URL'
        return output
        log.error('INVALID URL')
        log.debug('CHECK YOUR URL')


if __name__ == '__main__':
    args = {'method': 'GET',
            'endpoint': 'https://google.com',
            'headers': {'Accept': 'application/json'},
            'body': None,
            'auth': (None, None),
            'params': ('application/json'),
            'log': 'INFO'
            }
    web_surfer(args)

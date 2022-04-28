import requests
import re
from main.loger import *


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
    # print(args)
    # print()
    output = {}
    method = args['method']
    url = args['endpoint']
    headers = args['headers']
    body = args['body']
    auth = args['auth']
    #auth_key = args['key_id']
    params = args['params']
    log_level = args['log']
    #logger_start(log_level)
    log.info('Arguments parsed')
    methods = dict(GET=get_method(url, auth, params, headers), POST=post_method(url, auth, body, headers),
                   PUT=put_method(url, auth, body, headers), PATCH=patch_method(url, auth, body, headers),
                   DELETE=delete_method(url))
    #valid_url = r'^(http|https)(://)\w+\S+$'
    par = re.compile(
        r'^(?:http|ftp)s?://'
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
        r'localhost|'
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        r'(?::\d+)?'
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    if isinstance(url, str) and re.match(par, url):
        log.info(f'URL valid. Sending request to: {url}')
        req = methods[method]
        if isinstance(req, list):
            output['Error'] = req[0]
            log.error('Connection ERROR!')
            log.debug('Please try another URL')
            return output
            #print(output)  # output
        else:
            log.info('Connection established')
            output['URL'] = req.url
            output['Response Status'] = req.reason
            output['Response Status Code'] = req.status_code
            log.info(f'Method: {method} - Endpoint: {req.url}')
            log.info(f'RESPONSE CODE: {req.status_code} - STATUS: {req.reason}')

            output['Response Time'] = round(req.elapsed.total_seconds(), 2)
            #output['Body'] = body
            #output['headers'] = req.headers
            #log.info('DATA collected sucessfully')
            if req.headers.get('content-type')[:16] == 'application/json':
                log.info('JSON content found')
                log.info('DATA collected successfully')
                #log.debug('test')
                output['JSON'] = 'OK'
                return output, req.content, req.json
            else:
                log.error('JSON content not found')
                log.debug('No JSON data, please try another url or set correct parameters')
                log.info('DATA collected successfully')
                output['JSON'] = 'NOT FOUND'
                return output, req.content
    else:
        output['Error'] = 'Invalid URL'
        log.error('INVALID URL')
        log.debug('CHECK YOUR URL')
        return output


# if __name__ == '__main__':
#     args = {'method': 'GET',
#             'endpoint': 'https://google.com',
#             'headers': None,
#             'body': None,
#             'auth': (None, None),
#             'params': None,
#             'log': None
#             }
#     print(web_surfer(args))

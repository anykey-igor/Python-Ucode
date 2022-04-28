import re
import requests
from helper import print_stderr, print_stdout


# def request(url):
#     try:
#         rs = requests.get(url)
#         print_stdout(f"Request to the '{url}' has been sent")
#         if rs.status_code == 200:
#             print_stdout(rs)
#         elif rs.status_code == 404:
#             print_stdout(rs)
#             print_stderr(f"Request failed")
#             return 1
#         return rs
#     except Exception as error:
#         print_stderr(f"{error}")
#         return 1

def write_to_file(set_file, text_con):
    try:
        with open(set_file, 'wb+') as f:
            # print_stdout(f"Parsing page data")
            # print_stdout(f"Page data has been parsed")
            # print_stdout(f"Saving page data to '{set_file}'")
            f.write(text_con)
            # print_stdout(f"Page data has been saved")
    except Exception as error:
        return print_stderr(error)


def html_save(get_url, set_file):
    regex = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    if re.match(regex, get_url) is None:
        message = b"ERROR| The site URL format is invalid"
        print_stderr(f"The site URL format is invalid")
        return write_to_file(set_file, message)
    else:
        print_stdout(f"Sending the request to the '{get_url}'")
        try:
            rq = requests.get(get_url)

            if rq.status_code == 200:
                print_stdout(f"Request to the '{get_url}' has been sent")
                print_stdout(f"{rq}")
                print_stdout(f"Parsing page data")
                print_stdout(f"Page data has been parsed")
                print_stdout(f"Saving page data to '{set_file}'")
                write_to_file(set_file, rq.content)
                print_stdout(f"Page data has been saved")
                return write_to_file(set_file, rq.content)
            elif rq.status_code <= 404:
                print_stdout(f"Request to the '{get_url}' has been sent")
                print_stdout(f"{rq}")
            else:
                print_stderr(f"{rq}")
                #print_stdout(rq.status_code)
                print_stderr(f"Request failed")
        except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError) as error:
            message = f"ERROR| "+ str(error)+ "\n"
            #message_b= message.encode()
            print_stderr(error)
            #write_to_file(set_file, message_b)

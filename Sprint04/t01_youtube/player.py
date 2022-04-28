import webbrowser
import re
import sys
from helper import print_stderr, print_stdout


regex = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)


if len(sys.argv) == 1:
    print_stderr('The site URL was not passed.')
    sys.exit()
else:
    youtube_link = str(sys.argv[1])
    #regex = r"https:\/\/(?:youtu\.be\/|(?:[a-z]{2,3}\.)?youtube\.com\/watch(?:\?|#\!)v=)([\w-]{11}).*"
    regex = r"^(?:http|https)://www.(?:youtube.com)/[\w?=/]+$"
if re.match(regex, youtube_link) is None:  # validates URL that is passed to it using a validation regex
    print_stderr('The URL is invalid.')
else:
    print_stdout(f"Opening the YouTube video at {youtube_link}.")
    webbrowser.open(youtube_link)
    print_stdout(f'YouTube video opened.')

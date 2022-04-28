import re


def write_file(file_name=str, message='None'):
    file_name = str(file_name)
    pattern = r'^[\w]+.txt$'
    if re.findall(pattern, file_name):
        try:
            with open(file_name, "w+") as wf:
                wf.write(message)
            with open(file_name, "r+") as rf:
                data = rf.read()
        except PermissionError:
            print(f'Failed to read file "{file_name}".')
        except FileNotFoundError:
            print(f'File not found - {file_name}')
        else:
            if data == message:
                print(f'Your message has been written to file "{file_name}".')
                print(f'File "{file_name}" now contains the following text:')
                print(f'{data}')
            else:
                print(f"'Something went wrong...'")
    else:
        print(f'Please enter the filename in the format "filename.txt".')
        print(f'Failed to write to file "{file_name}".')

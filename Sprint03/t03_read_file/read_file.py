def read_file(file_name):
    try:
        with open(file_name, "r") as file:
            data = file.read()
        return print(f'File "{file_name}" has the following message:\n{data}')
    except (PermissionError, FileNotFoundError, OSError):
        return print(f'Failed to read file "{file_name}".')

import re

def check_address(check_dict):
    reg_index = r'^\S*Ukraine\s*,\s*[A-Za-z-[ ]{1,}\s*,\s*(?:\D[A-Za-z ]*)\s{1,}\d{1,6}\s*,\s*\d{5}$'
    #reg_index = '^(Ukraine\s*),([ \w]\D+),([ ]*[a-zA-Z _-]+[ ]+\d{1,6}),([ ]*\d{5})$'
    #reg_index = '^(Ukraine\s*)+,([ ]*\w+\D),([ ]*[a-zA-Z _-]+[ ]+\d{1,6})+,([ ]*\d{5})+$'
    #reg_index = '^(Ukraine\s*),([ ]+\w+\D)+,([ ]*[a-zA-Z _-]+[\s]\d{1,6})+,([ ]*\d{5})+$'
    fol_list = []
    for key_dict in check_dict:
        if re.findall(reg_index, check_dict[key_dict]):
            fol_list.append(f"The address of {key_dict} is valid.")
        else:
            fol_list.append(f"The address of {key_dict} is invalid.")


    return fol_list

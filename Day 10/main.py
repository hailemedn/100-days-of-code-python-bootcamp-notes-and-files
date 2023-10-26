# functions with outputs
# function with multiple outputs
# return indicates the end of the function
# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return "You didn't provie valid inputs."
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} {formated_l_name}"

# print(format_name("AnGelA", "YU"))

# code challenge days in a month.py


def format_name(f_name, l_name):
# Docstrings - used to write the documentation for the function
    '''Take a first and last name and format it to return the title case version of the name'''
    if f_name == "" or l_name == "":
        return "You didn't provie valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

# multi line comment unrecommended
'''
comment
another line comment
comment
'''

# multi line comment recommended
# comment
# another line comment
# another line comment


# return vs print inside function
    # return suitable when u need to do further calculation with the output of the function
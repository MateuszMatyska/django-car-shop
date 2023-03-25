def is_argument_int(argument):
    flag = True
    try:
        int(argument)
    except ValueError:
        flag = False
    
    return flag

def is_argument_float(argument):
    flag = True
    try:
        float(argument)
    except ValueError:
        flag = False
    
    return flag

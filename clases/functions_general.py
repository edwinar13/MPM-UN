import re

# ::::::::::::::::::::   VERIFICACION ::::::::::::::::::::
def IsNumber(value):
    x=re.search("^[0-9]+([.][0-9]+)?$",value)
    if x != None:
        return True
    else:
        return False

    """
    validacion = False
    try:
        valueF = float(value)
        validacion = True
    except Exception as e:
        print('no es nuemero: {}'.format(e))

    return validacion
    """
def addZeroNumber(value):
    len_value=len(value)
    point_index=value.find('.')
    if point_index == 0:
        value = "0{}".format(value)
    elif point_index == (len_value-1):
        value = "{}0".format(value)
    return value
"""Este módulo contiene las funciones generales.

func:
    : isNumber. 

"""
import re

def isNumber(value):
    """verificar si es un número.

    Args:
        value (str,int,float): cadena que contiene el número.

    Returns:
        (bool): 
            : True >> si es un número.
            : False >> si no es un número.
            
    """       
    validate = False
    try:
        valueF = float(value)
        validate = True
    except Exception as e:
        pass
    return validate   
    """
    x=re.search("^[0-9]+([.][0-9]+)?$",value)
    if x != None:
        return True
    else:
        return False
    """

    """Función que agrega un cero a un numero decimal (str) con forma [1.] o [.1].

    Args:
        value (str): cadena que contiene el numero.

    Returns:
        (str): una cadena con el numero que incluye el cero [1.0] o [0.1]
    """    
    len_value=len(value)
    point_index=value.find('.')
    if point_index == 0:
        value = "0{}".format(value)
    elif point_index == (len_value-1):
        value = "{}0".format(value)
    return value
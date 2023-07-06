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

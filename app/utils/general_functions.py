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

def format_number(number):
    """Formatear un número para mostrarlo en la interfaz gráfica.
     
     args:
        number (float): Número a formatear.
    
    returns:
        (str): Número formateado.      
        
    """

    integer_format = "{:.0f}"
    common_format = "{:.1f}"
    decimal_format = "{:.6f}"
    scientific_format = "{:.2e}"

    if abs(number) < 0.00001:
        return scientific_format.format(number)
        
    elif abs(number) < 1:
        return decimal_format.format(number)
    
    elif abs(number) < 100:
        return common_format.format(number)
    
    elif abs(number) < 99999:
        return integer_format.format(number)
    else:
        return common_format.format(number)
    '''
    if abs(number) < 0.000001 or abs(number) > 999999:
        return scientific_format.format(number)
    '''

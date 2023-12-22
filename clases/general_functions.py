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
    # Define a format for common output with three decimals
    common_format = "{:.3f}"

    # Define a format for output in scientific notation with one decimal
    scientific_format = "{:.2e}"

    # Format the number according to the defined rules
    if abs(number) < 0.001 or abs(number) > 999:
        return scientific_format.format(number)
    else:
        return common_format.format(number)

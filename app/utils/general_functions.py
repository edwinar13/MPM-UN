"""Este módulo contiene las funciones generales.

func:
    : isNumber. 

"""
import re

# Resultados escalares (sin componente xx/yy/xy): tipo del menú → clave guardada
SCALAR_RESULTS = {'eqplas': 'EQPLAS', 'pp': 'PRESIONPOROS'}

# Opciones del menú de gráficas en el tiempo: texto mostrado (también rótulo del
# eje y) → clave guardada en RESULTADOSNODOS. Las magnitudes se guardan como *XY.
GRAPH_RESULTS = {
    'Coordenada X (m)': 'CORX',
    'Coordenada Y (m)': 'CORY',
    'Desplazamiento X (m)': 'DESPLXX',
    'Desplazamiento Y (m)': 'DESPLYY',
    'Desplazamiento total (m)': 'DESPLXY',
    'Velocidad X (m/s)': 'VELXX',
    'Velocidad Y (m/s)': 'VELYY',
    'Velocidad total (m/s)': 'VELXY',
    'σxx (kPa)': 'SIGXX',
    'σyy (kPa)': 'SIGYY',
    'τxy (kPa)': 'SIGXY',
    'Def. elástica εxx': 'EPSEXX',
    'Def. elástica εyy': 'EPSEYY',
    'Def. elástica εxy': 'EPSEXY',
    'Def. plástica εxx': 'EPSPXX',
    'Def. plástica εyy': 'EPSPYY',
    'Def. plástica εxy': 'EPSPXY',
    'Def. plástica equivalente': 'EQPLAS',
    'Presión de poros (kPa)': 'PRESIONPOROS',
}

# Columnas de la tabla resumen y del csv: nodo, tiempo y los mismos resultados de la gráfica
TABLE_COLUMNS = ['Nodo', 'Tiempo'] + list(GRAPH_RESULTS)


def table_rows(result_nodes, times):
    """Filas (listas de texto) de la tabla resumen: una por nodo y tiempo. Un
    resultado que no está guardado (p. ej. presión de poros) queda vacío."""
    keys = list(GRAPH_RESULTS.values())
    for node, data in result_nodes.items():
        series = [data.get(k) for k in keys]
        for i, t in enumerate(times):
            yield [str(node), f"{t:.6g}"] + ["" if s is None else f"{s[i]:.6e}" for s in series]


def result_key(type_result, axis):
    """Clave del resultado guardado ('SIGXX', 'EQPLAS', 'PRESIONPOROS', ...)
    para un tipo del menú de animación y un eje ('xx', 'yy', 'xy')."""
    if type_result in SCALAR_RESULTS:
        return SCALAR_RESULTS[type_result]
    return f'{type_result}{axis}'.upper()


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

import pandas as pd

# lê dados numéricos em formato br e transforma em float
def br_to_float(valor):
    if isinstance(valor, str): 
        valor = valor.strip() 
        if valor == "": 
            return None
        return float(valor.replace('.', '').replace(',', '.'))
    return valor

# extrai os pontos em números
def extract_dots(valor):
    return valor.replace('.','')
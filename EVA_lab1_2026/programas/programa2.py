# -*- coding: utf-8 -*-
import re
import sys
from programa1 import programa1

def programa2(RutaFactura):
    
    '''
    SU CÓDIGO
    
    NOTA: El formato de la fecha debe ser AAAA-MM-DD 
    '''
    text = programa1(RutaFactura)
    pattern = r"(\d{2})-(\d{2})-(\d{4})"
    fecha = re.search(pattern, text)
    norm = fecha.group(3) + '-' + fecha.group(2) + '-' + fecha.group(1)
    monto = re.findall(r'\d+\,\d{2}', text)
    return norm, monto
  

if __name__ == '__main__':
    entrada = sys.argv[1]  # archivo entrada (param)
    salida = sys.argv[2]   # archivo salida (param)
    
    fecha,monto = programa2(entrada)      # ejecutar 
    ret =f"Fecha: {fecha} | Monto: {monto}"
    f = open(salida, 'w')  # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida

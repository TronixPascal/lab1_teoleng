# -*- coding: utf-8 -*-
import re
import sys
from programa2 import programa2
from programa4 import programa4


def programa5(RutaPdf,RutaXML):
    resultado = False
    
    '''
    SU CÓDIGO
    '''
    texto_xml = programa4(RutaXML)

    fecha_pdf, monto_pdf = programa2(RutaPdf)
    match_fecha = re.search(fecha_pdf, texto_xml, flags=0)
    match_monto = re.search(monto_pdf, texto_xml, flags=0)
    if match_fecha and match_monto:
        resultado = True
    
    if resultado:
        return(True)
    else:
        return(False)

if __name__ == '__main__':
    entrada_pdf = sys.argv[1]  # archivo entrada (param)
    entrada_xml = sys.argv[2]  # archivo entrada (param)
    salida = sys.argv[3]   # archivo salida (param)    
 
    ret = programa5(entrada_pdf,entrada_xml)      # ejecutar 
    if (ret):
        ret = "Encontrado"
    else:
        ret = "No encontrado"
    
    f = open(salida, 'w')  # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
